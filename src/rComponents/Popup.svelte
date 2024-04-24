<!-- Popup.svelte -->
<script>
  import Student from "./Logogram.svelte";
  import { describeStudent } from "../utils/utils.js";
  export let student;
  export let visible;
  export let onClose;

  function getSrc(key) {
    console.log(student.grams, key);
    if (!student?.grams?.[key]) return;

    return `./images/translator/${student.grams[key].id}.png`;
  }

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
      <div class="symbols-container">
        {#each Object.keys(student.grams) as value}
          {#if getSrc(value) !== undefined}
            <img class="image-container-logogram" src={getSrc(value)} alt="" />
          {/if}
        {/each}
      </div>
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
    display: flex;
    position: relative;
    background-color: transparent;
    align-items: center;
  }

  .image-container-logogram {
    width: 80px;
    height: 80px;
    max-width: 100%;
    display: flex;
    position: relative;
  }

  .text-symbol {
    font-family: "Gotham Light", sans-serif; /* Fallback to sans-serif if Gotham Light is not available */
    font-size: 24px;
    font-weight: normal; /* Make sure to set font-weight to normal if you're using a specific font weight */
    text-overflow: ellipsis;
    white-space: nowrap;
    align-items: center;
    margin-block-end: 0px;
  }
</style>
