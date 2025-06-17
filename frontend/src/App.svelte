<script>
  import { onMount } from 'svelte';
  let records = [];
  let loading = true;
  let error = '';

  onMount(async () => {
    try {
      const res = await fetch('http://localhost:8000/api/v1/record/records/');
      if (!res.ok) throw new Error('Error en la petición');
      records = await res.json();
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  });
</script>

{#if loading}
  <p>Cargando...</p>
{:else if error}
  <p style="color:red">{error}</p>
{:else}
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Creado</th>
        <th>Actualizado</th>
        <th>Pedimento</th>
        <th>Organización</th>
      </tr>
    </thead>
    <tbody>
      {#each records as record}
        <tr>
          <td>{record.id}</td>
          <td>{record.created_at}</td>
          <td>{record.updated_at}</td>
          <td>{record.pedimento}</td>
          <td>{record.organizacion}</td>
        </tr>
      {/each}
    </tbody>
  </table>
{/if}