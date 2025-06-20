import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function LogoutButton() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    // Elimina otros datos de sesión si los tienes
    navigate('/login');
  };

  return (
    <button onClick={handleLogout} style={{marginTop: '1rem'}}>
      Cerrar sesión
    </button>
  );
}
