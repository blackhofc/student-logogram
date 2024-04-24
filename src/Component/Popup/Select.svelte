<!-- Popup.svelte -->
<script>
  import Container from "../Container.svelte";

  import { describeStudent } from "../../utils/utils.js";

  export let student;
  export let visible;
  export let onClose;
  let style = `mask-image: url(${student?.symbol}); background-image: linear-gradient(to bottom right, ${student?.gradient});`;

  function getSrc(key, value) {
    if (!student?.grams?.[key]?.[value]) return;
    console.log(
      { key, value },
      `./images/translator/${student.grams[key][value].id}.png`
    );

    return `./images/translator/${student.grams[key][value].id}.png`;
  }

  function closePopup(value) {
    onClose();
  }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
{#if visible}
  {(style = `mask-image: url(${student?.symbol}); background-image: linear-gradient(to bottom right, ${student?.gradient});`)}
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="popup-overlay" on:click={closePopup}>
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="popup-content" on:click|stopPropagation>
      <h2 class="text-title">{student.name}</h2>
      <p class="text-sub">{describeStudent(student)}</p>

      <div class="card-container">
        <div class="gradient-image" {style}></div>
      </div>

      <div class="symbols-container">
        {#each Object.keys(student.grams) as key}
          {#each Object.entries(student.grams[key]) as [name, symbol]}
            <Container {name} {symbol} />
          {/each}
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
    z-index: 1500;
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
    max-width: 90vw;
    max-height: 90vh;
    overflow-x: auto;
    overflow-y: auto;
  }

  .symbols-container {
    width: 100%;
    height: 100%;
    display: flex;
    position: relative;
    background-color: transparent;
    align-items: center;
    flex-wrap: wrap;
    justify-content: space-around;
  }

  .card-container {
    height: 100%;
    width: 100%;
    /*background: linear-gradient(to bottom right, #ff9999, #66ccff, #99ff99); */
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    border: 0px solid black;
  }

  .gradient-image {
    width: 350px;
    height: 350px;
    -webkit-mask-size: cover;
    mask-position: center;
    mask-repeat: no-repeat;
    mask-size: 100%;
    mask-mode: alpha;
    color: transparent;
    background-size: 200% 200%;
    animation: animateGradient 10s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    background-size: 200% 200%;
    background-position: 0% 100%;
    animation-direction: alternate;
  }

  @keyframes animateGradient {
    0% {
      background-position: 200% 50%;
    }
    50% {
      background-position: 0% 50%;
    }
    100% {
      background-position: -200% 50%;
    }
  }
  /* width */
  ::-webkit-scrollbar {
    height: 7px;
    width: 7px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 1px grey;
    border-radius: 0px;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #969696;
    border-radius: 0px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #141414;
  }
</style>
