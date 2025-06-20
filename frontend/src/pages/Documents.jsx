import React, { useEffect, useState } from 'react';
import { fetchDocuments } from '../api/documents';
import { useNotification } from '../context/NotificationContext';
import { Link } from 'react-router-dom';

const API_URL = import.meta.env.VITE_EFC_API_URL;

const downloadFile = async (id, filename = 'archivo', setSuccess, setError, showMessage) => {
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
  if (setSuccess) setSuccess('Descarga exitosa');
};

export default function Documents() {
  const [pedimentos, setPedimentos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const { showMessage } = useNotification();

  useEffect(() => {
    const token = localStorage.getItem('access');
    fetchDocuments(token)
      .then(data => {
        setPedimentos(data);
        setLoading(false);
      })
      .catch(err => {
        if (err.message === 'SESSION_EXPIRED') {
          localStorage.removeItem('access');
          localStorage.removeItem('refresh');
          showMessage('Tu sesión ha expirado, por favor inicia sesión de nuevo.', 'error');
          setTimeout(() => {
            window.location.href = '/login';
          }, 2000);
        } else {
          setError(err.message);
        }
        setLoading(false);
      });
  }, [showMessage]);

  if (loading) return <p>Cargando documentos...</p>;
  if (error) return <p style={{color:'red'}}>{error}</p>;

  return (
    <div>
      <h2>Lista de Pedimentos y Documentos</h2>
      {success && <p style={{color:'green'}}>{success}</p>}
      {pedimentos.length === 0 ? (
        <p>No hay pedimentos.</p>
      ) : (
        <table border="1" cellPadding="8" style={{margin:'auto', width:'100%', marginBottom:'2rem'}}>
          <thead>
            <tr>
              <th>Pedimento</th>
              <th>Fecha de pago</th>
              <th>Contribuyente</th>
              <th>Alerta</th>
              <th>CURP Apoderado</th>
              <th>Importe total</th>
              <th>Saldo disponible</th>
              <th>Importe pedimento</th>
              <th>Expediente</th>
            </tr>
          </thead>
          <tbody>
            {pedimentos.map(ped => (
              <tr key={ped.id}>
                <td>
                  <Link to={`/documents/pedimento/${ped.id}`}>{ped.pedimento}</Link>
                </td>
                <td>{ped.fechapago}</td>
                <td>{ped.contribuyente}</td>
                <td>{ped.alerta ? 'Sí' : 'No'}</td>
                <td>{ped.curp_apoderado}</td>
                <td>{ped.importe_total}</td>
                <td>{ped.saldo_disponible}</td>
                <td>{ped.importe_pedimento}</td>
                <td>{ped.existe_expediente ? 'Sí' : 'No'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
