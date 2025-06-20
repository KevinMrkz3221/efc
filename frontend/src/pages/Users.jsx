import React, { useEffect, useState } from 'react';
import { fetchUsers, createUser, updateUser, deleteUser } from '../api/users';
import { useNotification } from '../context/NotificationContext';

const initialForm = {
  username: '',
  email: '',
  first_name: '',
  last_name: '',
  password: '',
};

export default function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [form, setForm] = useState(initialForm);
  const [editingId, setEditingId] = useState(null);
  const { showMessage } = useNotification();

  const token = localStorage.getItem('access');

  const loadUsers = () => {
    setLoading(true);
    fetchUsers(token)
      .then(data => {
        setUsers(data);
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
  };

  useEffect(() => {
    loadUsers();
    // eslint-disable-next-line
  }, [showMessage]);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      if (editingId) {
        await updateUser(token, editingId, form);
        showMessage('Usuario actualizado', 'success');
      } else {
        await createUser(token, form);
        showMessage('Usuario creado', 'success');
      }
      setForm(initialForm);
      setEditingId(null);
      loadUsers();
    } catch (err) {
      showMessage(err.message, 'error');
    }
  };

  const handleEdit = user => {
    setForm({
      username: user.username,
      email: user.email,
      first_name: user.first_name,
      last_name: user.last_name,
      password: '', // No se muestra el password actual
    });
    setEditingId(user.id);
  };

  const handleDelete = async id => {
    if (!window.confirm('¿Seguro que deseas eliminar este usuario?')) return;
    try {
      await deleteUser(token, id);
      showMessage('Usuario eliminado', 'success');
      loadUsers();
    } catch (err) {
      showMessage(err.message, 'error');
    }
  };

  if (loading) return <p>Cargando usuarios...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div>
      <h2>Usuarios de la organización</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: '2rem' }}>
        <input name="username" value={form.username} onChange={handleChange} placeholder="Usuario" required />{' '}
        <input name="email" value={form.email} onChange={handleChange} placeholder="Email" required type="email" />{' '}
        <input name="first_name" value={form.first_name} onChange={handleChange} placeholder="Nombre" />{' '}
        <input name="last_name" value={form.last_name} onChange={handleChange} placeholder="Apellido" />{' '}
        <input name="password" value={form.password} onChange={handleChange} placeholder="Contraseña" type="password" required={!editingId} />{' '}
        <button type="submit">{editingId ? 'Actualizar' : 'Crear'}</button>
        {editingId && <button type="button" onClick={() => { setForm(initialForm); setEditingId(null); }}>Cancelar</button>}
      </form>
      <table border="1" cellPadding="8" style={{ margin: 'auto' }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Usuario</th>
            <th>Email</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Foto de perfil</th>
            <th>Organización</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.username}</td>
              <td>{user.email}</td>
              <td>{user.first_name}</td>
              <td>{user.last_name}</td>
              <td>
                {user.profile_picture ? (
                  <img src={user.profile_picture} alt="profile" width={40} height={40} style={{borderRadius: '50%'}} />
                ) : 'Sin foto'}
              </td>
              <td>{user.organizacion}</td>
              <td>
                <button onClick={() => handleEdit(user)}>Editar</button>{' '}
                <button onClick={() => handleDelete(user.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
