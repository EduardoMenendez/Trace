<script>
    export let message = "";
    export let visible = false;
    export let onDismiss = () => {};
  </script>
  
  {#if visible}
    <div class="alert-overlay">
      <div class="alert-box">
        <p>{message}</p>
        <button on:click={onDismiss}>Close</button>
      </div>
    </div>
  {/if}
  
  <style>
    .alert-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }
    .alert-box {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      text-align: center;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      max-width: 90%;
    }
    .alert-box p {
      margin-bottom: 10px;
      font-size: 16px;
    }
    .alert-box button {
      background: #4aa6b0;
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 14px;
    }
    .alert-box button:hover {
      background: #357f8a;
    }
  </style>
  