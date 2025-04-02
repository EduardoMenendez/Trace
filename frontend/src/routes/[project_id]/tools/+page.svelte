<script>
  // @ts-ignore
  import { page } from '$app/stores';
  import {projects} from '$lib/data/projects';
  
  const project = projects.find((value)=>value.id===$page.params.project_id);
  console.log(project);
  const icons = {
    check: '<svg style="background:none" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M20.285 6.709a1 1 0 0 0-1.414-1.418l-9.192 9.192-4.242-4.242a1 1 0 0 0-1.415 1.414l5 5a1 1 0 0 0 1.415 0l9.848-9.846z"/></svg>'
  }
</script>

<div class="tool-home">
<h1 class="title">Tools</h1>
<div class="subtitle">
  <h3>{project?.title}</h3>
</div>
<div class="tool-wrapper">
  <div class="tool-list">
    <div class="tool-row">
      <div class="tool-name">HTTP Tester</div>
      <div class="tool-details">
        <span class="status completed">{@html icons.check}</span>
        <div class="tool-status">
          <span class="progress-text"><span class="bold">100%</span> Completed</span>
          <div class="progress-bar">
            <div class="progress-fill" style="width: 100%; background-color: #22c55e;"></div>
          </div>
        </div>
        <div class="tool-actions">
          <a class="info">Info</a>
          <a class="view" href="./tools/HttpClient">View</a>
        </div>
      </div>
    </div>
  </div>
</div>
</div>

<style>
.tool-home {
  display: flex;
  flex-direction: column;
  width: 100%;
  padding: 50px;
}
.tool-wrapper{
  width: 100%;
  display: flex;
  justify-content: center;
}
.title {
  font-size: 2.5em;
  font-weight: 600;
  margin-bottom: 20px;
}
.subtitle{
  margin-bottom: 2rem;
  width: 100%;
  text-align: left;
  max-width: 1000px;
}
.completed{
  font-weight: 2rem;
  background-color: #20a453;
  color: white;
  padding: 0.8rem;
  border-radius: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.bold{
  font-weight: bold;
  background: none;
  font-size: 1.5rem;
}
.tool-list {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 1rem;
}

.tool-details{
  background: none;
  display: flex;
  width: 40%;
  align-items: center;
  justify-content: center;
}
.tool-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  justify-content: center;
  background-color: #e1e1e1;
  padding: 1rem;
  padding-inline: 2rem;
  border-radius: 0.75rem;
}
.tool-name,.tool-status, .tool-status>:not(marquee),.progress-bar,.tool-actions{
  background: none;
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
  width: 50%;
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
  height: 10px;
  width: 70%;
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
  gap: 2rem;
}

.info,
.view {
  padding: 0.5rem 2rem;
  border-radius: 0.5rem;
  cursor: pointer;
  text-decoration: none;
}

.info {
  background-color: transparent;
  color: #4aa6b0;
}
.info:hover{
  color: #387773;
}

.view {
  background-color: #4aa6b0;
  color: white;
}

.view:hover {
  background-color: #499b96;
}
</style>