<script>
    import { page } from '$app/stores';
    import {projects} from '$lib/data/projects';
    
    const project = projects.find((value)=>value.id===$page.params.project_id);
    console.log(project);
</script>

<div class="tool-home">
  <h1 class="title">Tools</h1>
  <div class="subtitle">
    <h3>{project?.title}</h3>
  </div>
  <div class="tool-list">
    <div class="tool-row">
      <div class="tool-name">HTTP Tester</div>
      <div class="tool-status">
        <span class="status completed">✔</span>
        <span class="progress-text">100% Completed</span>
        <div class="progress-bar">
          <div class="progress-fill" style="width: 100%; background-color: #22c55e;"></div>
        </div>
      </div>
      <div class="tool-actions">
        <a class="info">Info</a>
        <a class="view" href={`/${project.id}/tools/HttpClient`}>View</a>
      </div>
    </div>
  </div>
</div>

<style>
  .tool-home {
    display: flex;
    padding: 2rem;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .title {
    font-size: 2rem;
    margin-bottom: 2rem;
    width: 100%;
    text-align: left;
    max-width: 1000px;
  }
  .subtitle{
    margin-bottom: 2rem;
    width: 100%;
    text-align: left;
    max-width: 1000px;
  }


  .tool-list {
    width: 100%;
    max-width: 1000px;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .tool-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #f4f4f5;
    padding: 1rem;
    border-radius: 0.75rem;
  }

  .tool-name {
    font-weight: 600;
    flex: 1;
  }

  .tool-status {
    display: flex;
    flex-direction: column;
    flex: 2;
    padding: 0 1rem;
  }

  .status {
    font-weight: bold;
    margin-bottom: 0.25rem;
  }

  .progress-text {
    font-size: 0.875rem;
    margin-bottom: 0.25rem;
  }

  .progress-bar {
    height: 6px;
    width: 100%;
    background-color: #e5e7eb;
    border-radius: 4px;
    overflow: hidden;
  }

  .progress-fill {
    height: 100%;
    transition: width 0.3s ease-in-out;
  }

  .tool-actions {
    display: flex;
    gap: 0.75rem;
  }

  .info,
  .view {
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: 500;
    font-size: 0.875rem;
    cursor: pointer;
    text-decoration: none;
  }

  .info {
    background-color: transparent;
    color: #6b7280;
  }

  .view {
    background-color: #5fb5b0;
    color: white;
  }

  .view:hover {
    background-color: #499b96;
  }
</style>