import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Login from './pages/Login';
import Admin from './pages/Admin';
import RequireAuth from './components/RequireAuth';
import Landing from './pages/Landing';
import Documents from './pages/Documents';
import Organization from './pages/Organization';
import Users from './pages/Users';
import Reports from './pages/Reports';
import PedimentoDetail from './pages/PedimentoDetail';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/admin" element={
          <RequireAuth>
            <Admin />
          </RequireAuth>
        } />
        <Route path="/documents" element={
          <RequireAuth>
            <Documents />
          </RequireAuth>
        } />
        <Route path="/documents/pedimento/:id" element={
          <RequireAuth>
            <PedimentoDetail />
          </RequireAuth>
        } />
        <Route path="/mi-organizacion" element={
          <RequireAuth>
            <Organization />
          </RequireAuth>
        } />
        <Route path="/usuarios" element={
          <RequireAuth>
            <Users />
          </RequireAuth>
        } />
        <Route path="/reportes" element={
          <RequireAuth>
            <Reports />
          </RequireAuth>
        } />
        {/* otras rutas */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;