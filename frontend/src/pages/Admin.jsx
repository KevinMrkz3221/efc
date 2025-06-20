import React from 'react';
import LogoutButton from '../components/LogoutButton';
import Navbar
 from '../components/Navbar';
export default function Admin() {
  return (
    <div>
      <h2>Panel de Administración</h2>
      <LogoutButton />
      <p>Bienvenido al panel de administración.</p>
    </div>
  );
}
