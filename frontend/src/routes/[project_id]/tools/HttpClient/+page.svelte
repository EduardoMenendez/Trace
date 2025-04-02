<script>
  import { page } from '$app/stores';
  import { projects } from '$lib/data/projects';

  const project = projects.find((value) => value.id === $page.params.project_id);
  console.log(project);
</script>

<div class="http-client">
    <h1 class="title">HTTP Tester</h1>  
    <div class="form-wrapper">
    <form>
        <h3 class="title2">Configuration</h3>
      <label>Target URL <input type="url" placeholder="https://google.com" required /></label>
      <div class="radio-group">
        <label>HTTP Method</label>
        <label><input type="radio" name="method" value="GET" checked /> GET</label>
        <label><input type="radio" name="method" value="PUT" /> PUT</label>
        <label><input type="radio" name="method" value="POST" /> POST</label>
      </div>
      <label>Header <input type="text" placeholder="application/json" /></label>
      <label>Cookies <input type="text" placeholder="csrf_token" /></label>
      <label>Hide Status Code <input type="text" placeholder="403, etc." /></label>
      <label>Show Only Status Code <input type="text" placeholder="200, 500, etc." /></label>
      <label>Proxy <input type="text" placeholder="https://proxy.example.com:3128" /></label>
      <label>Request Body <input type="text" placeholder="NULL" /></label>
      <label>Additional Parameters <input type="text" placeholder="NULL" /></label>

      <button type="submit">Start</button>
    </form>
  </div>
</div>

<style>
    .http-client {
    display: flex;
    flex-direction: column; 
    align-items: center;
    padding: 2rem;
    width: 100%;
    }
    .title {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 2rem;
    width: 100%;
    }

    .form-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    }

  form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    width: 100%;
    max-width: 700px;
  }
  label {
    font-weight: 500;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }
  input[type="text"],
  input[type="url"] {
    font-size: 1.1rem;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;
    border: 1px solid #ccc;
  }

    .radio-group {
    display: flex;
    gap: 3.5rem;
    align-items: center;
    flex-wrap: wrap;
    }

  button {
    align-self: flex-start;
    padding: 0.9rem 2rem;
    border: none;
    border-radius: 0.5rem;
    background-color: #5fb5b0;
    color: white;
    font-weight: bold;
    font-size: 1.1rem;
    cursor: pointer;
  }

  button:hover {
    background-color: #499b96;
  }
</style>
