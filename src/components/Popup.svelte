<!-- Popup.svelte -->
<script>
  import Student from "./Student.svelte";
  import { describeStudent } from "../utils/utils.js";
  export let student;
  export let visible;
  export let onClose;

  function closePopup(value) {
    onClose();
  }
</script>

{#if visible}
  <div class="popup-overlay" on:click={closePopup}>
    <div class="popup-content" on:click|stopPropagation>
      <h2 class="text-title">{student.name}</h2>
      <p class="text-sub">{describeStudent(student)}</p>
      <Student {student} />
      <div class="symbols-container"></div>
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
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: column;
  }

  .symbols-container {
    width: 100%;
    height: 100px;
    background-color: black;
  }
</style>
