<!-- Popup.svelte -->
<script>
  export let visible;
  export let onClose;

  function closePopup() {
    onClose();
  }
</script>

{#if visible}
  <div class="popup-overlay" on:click={closePopup}>
    <div class="popup-content" on:click|stopPropagation>
      <slot />
    </div>
  </div>
{/if}

<style>
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Semi-black background */
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .popup-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-left: 10%;
    margin-right: 10%;
  }
</style>
