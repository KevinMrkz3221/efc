import React, { useEffect, useState } from 'react';
import { fetchOrganizationUsage } from '../api/organizacion';
import { useNotification } from '../context/NotificationContext';

export default function Organization() {
  const [info, setInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const { showMessage } = useNotification();

  useEffect(() => {
    const token = localStorage.getItem('access');
    fetchOrganizationUsage(token)
      .then(data => {
        setInfo(data);
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

  if (loading) return <p>Cargando información de la organización...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div>
      <h2>Mi Organización</h2>
      <ul>
        <li><b>Organización:</b> {info.organizacion}</li>
        <li><b>Límite de almacenamiento (GB):</b> {info.limite_almacenamiento_gb}</li>
        <li><b>Espacio utilizado (GB):</b> {info.espacio_utilizado_gb.toFixed(2)}</li>
        <li><b>Espacio disponible (MB):</b> {(info.espacio_disponible_bytes / (1024 * 1024)).toFixed(2)}</li>
        <li><b>Porcentaje utilizado:</b> {info.porcentaje_utilizado}%</li>
        <li><b>Total de Pedimentos:</b> {info.total_pedimentos}</li>
        <li><b>Total de documentos:</b> {info.total_documentos}</li>
        <li><b>Total de usuarios:</b> {info.total_usuarios}</li>
      </ul>
    </div>
  );
}
