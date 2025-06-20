import React from 'react';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';



export default function Navbar() {
  return (
    <nav style={{ padding: '1rem', background: '#f5f5f5', marginBottom: '2rem'}}>
      <Link to="/" style={{ marginRight: '1rem' }}>Inicio</Link>
      <Link to="/admin" style={{ marginRight: '1rem' }}>Admin</Link>
      <Link to="/login">Login</Link>
      <Link to="/documents" style={{ marginLeft: '1rem' }}>Documentos</Link>
      <Link to="/mi-organizacion" style={{ marginLeft: '1rem' }}>Mi Organización</Link>
      <Link to="/usuarios" style={{ marginLeft: '1rem' }}>Usuarios</Link>
      <Link to="/reportes" style={{ marginLeft: '1rem' }}>Reportes</Link>
    </nav>
  );
}
