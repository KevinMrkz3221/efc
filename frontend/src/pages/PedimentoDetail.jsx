import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useNotification } from '../context/NotificationContext';

const API_URL = import.meta.env.VITE_EFC_API_URL;

const downloadFile = async (id, filename = 'archivo', showMessage) => {
  const token = localStorage.getItem('access');
  const res = await fetch(`${API_URL}/api/v1/record/documents/descargar/${id}/`, {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });
  if (res.status === 401) {
    showMessage('Tu sesión ha expirado, por favor inicia sesión de nuevo.', 'error');
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    setTimeout(() => {
      window.location.href = '/login';
    }, 2000);
    return;
  }
  if (!res.ok) {
    alert('No autorizado o error en la descarga');
    return;
  }
  const blob = await res.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  window.URL.revokeObjectURL(url);
};

const downloadBulkZip = async (ids, showMessage, pedimentoNombre) => {
  if (!ids.length) {
    showMessage('Selecciona al menos un documento.', 'error');
    return;
  }
  const token = localStorage.getItem('access');
  const res = await fetch(`${API_URL}/api/v1/record/documents/bulk-download/`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ document_ids: ids, pedimento_nombre: pedimentoNombre }),
  });
  if (res.status === 401) {
    showMessage('Tu sesión ha expirado, por favor inicia sesión de nuevo.', 'error');
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    setTimeout(() => {
      window.location.href = '/login';
    }, 2000);
    return;
  }
  if (!res.ok) {
    showMessage('No autorizado o error en la descarga masiva', 'error');
    return;
  }
  const blob = await res.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${pedimentoNombre || 'documentos'}.zip`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  window.URL.revokeObjectURL(url);
};

export default function PedimentoDetail() {
  const { id } = useParams();
  const [pedimento, setPedimento] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selected, setSelected] = useState([]);
  const [downloading, setDownloading] = useState(false);
  const { showMessage } = useNotification();

  useEffect(() => {
    const token = localStorage.getItem('access');
    fetch(`${API_URL}/api/v1/customs/pedimentos/${id}/`, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })
      .then(res => {
        if (res.status === 401) {
          localStorage.removeItem('access');
          localStorage.removeItem('refresh');
          showMessage('Tu sesión ha expirado, por favor inicia sesión de nuevo.', 'error');
          setTimeout(() => {
            window.location.href = '/login';
          }, 2000);
          return null;
        }
        if (!res.ok) throw new Error('No autorizado o error en la petición');
        return res.json();
      })
      .then(data => {
        setPedimento(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, [id, showMessage]);

  if (loading) return <p>Cargando detalle de pedimento...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;
  if (!pedimento) return null;

  const allDocIds = pedimento.documentos ? pedimento.documentos.map(doc => doc.id) : [];
  const allSelected = selected.length === allDocIds.length && allDocIds.length > 0;

  const handleSelect = (id) => {
    setSelected(prev => prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id]);
  };

  const handleSelectAll = () => {
    if (allSelected) setSelected([]);
    else setSelected(allDocIds);
  };

  const handleBulkDownload = async (ids) => {
    setDownloading(true);
    await downloadBulkZip(ids, showMessage, pedimento?.pedimento);
    setDownloading(false);
  };

  return (
    <div>
      <h2>Detalle de Pedimento</h2>
      <p><b>Pedimento:</b> {pedimento.pedimento}</p>
      <p><b>Contribuyente:</b> {pedimento.contribuyente}</p>
      <p><b>Fecha de pago:</b> {pedimento.fechapago}</p>
      <p><b>Importe total:</b> {pedimento.importe_total}</p>
      <p><b>Saldo disponible:</b> {pedimento.saldo_disponible}</p>
      <p><b>Expediente:</b> {pedimento.existe_expediente ? 'Sí' : 'No'}</p>
      <h3>Documentos relacionados</h3>
      {allDocIds.length > 0 && (
        <>
          <button onClick={() => handleBulkDownload(allDocIds)} style={{marginBottom:'1rem', marginRight:'1rem'}} disabled={downloading}>
            {downloading ? 'Descargando...' : 'Descargar todos en ZIP'}
          </button>
          <button onClick={() => handleBulkDownload(selected)} style={{marginBottom:'1rem'}} disabled={selected.length === 0 || downloading}>
            {downloading ? 'Descargando...' : 'Descargar seleccionados en ZIP'}
          </button>
        </>
      )}
      {pedimento.documentos && pedimento.documentos.length > 0 ? (
        <table border="1" cellPadding="8" style={{margin:'auto', marginBottom:'1rem'}}>
          <thead>
            <tr>
              <th>
                <input type="checkbox" checked={allSelected} onChange={handleSelectAll} />
              </th>
              <th>ID</th>
              <th>Archivo</th>
              <th>Extensión</th>
              <th>Tamaño</th>
              <th>Creado</th>
              <th>Tipo</th>
              <th>Acción</th>
            </tr>
          </thead>
          <tbody>
            {pedimento.documentos.map(doc => (
              <tr key={doc.id}>
                <td>
                  <input type="checkbox" checked={selected.includes(doc.id)} onChange={() => handleSelect(doc.id)} />
                </td>
                <td>{doc.id}</td>
                <td>{doc.archivo}</td>
                <td>{doc.extension}</td>
                <td>{doc.size}</td>
                <td>{doc.created_at}</td>
                <td>{doc.document_type}</td>
                <td>
                  <button onClick={() => downloadFile(doc.id, doc.archivo.split('/').pop(), showMessage)}>
                    Descargar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Sin documentos relacionados.</p>
      )}
      <Link to="/documents">Volver a la lista</Link>
    </div>
  );
}
