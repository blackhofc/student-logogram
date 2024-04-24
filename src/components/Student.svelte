<!-- Student.svelte -->
<script>
  import { createEventDispatcher } from "svelte";

  export let student;
  let style = `mask-image: url(${student.symbol}); background-image: linear-gradient(to bottom right, #000, #000);`;

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("studentClicked", { detail: student });
  }

  function handleMouseOver() {
    console.log("HOVER", student.name);
    style = `mask-image: url(${student.symbol}); background-image: linear-gradient(to bottom right, ${student.gradient});`;
  }

  function handleMouseLeave() {
    console.log("LEAVE", student.name);
    style = `mask-image: url(${student.symbol}); background-image: linear-gradient(to bottom right, #000, #000);`;
  }

  function handleFocus() {
    handleMouseOver();
  }
</script>

<div
  class="flex-box"
  on:click={handleClick}
  on:keydown={null}
  tabindex="0"
  role="button"
  aria-label={`Click to view details of ${student.name}`}
  on:mouseover={handleMouseOver}
  on:mouseleave={handleMouseLeave}
  on:focus={handleFocus}
>
  <div class="card-container">
    <div class="gradient-image" {style}></div>
  </div>

  <p class="text-name">{student.name}</p>
</div>

<style>
  .flex-box {
    margin: 4px;
    width: 350px;
    height: 350px;
    display: flex;
    align-items: center;
    flex-direction: column;
  }

  .card-container {
    width: 100%;
    height: 100%;
    /*background: linear-gradient(to bottom right, #ff9999, #66ccff, #99ff99); */
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    position: relative;
    border: 0px solid black;
  }

  .text-name {
    font-family: "Gotham Light", sans-serif; /* Fallback to sans-serif if Gotham Light is not available */
    font-size: 16px;
    font-weight: normal; /* Make sure to set font-weight to normal if you're using a specific font weight */
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-bottom: 0px;
    margin-top: 5px;
  }

  .gradient-image {
    width: 350px;
    height: 350px;
    mask-size: 100%;
    cursor: pointer;
  }

  .text-name:hover {
    animation: expandName 0.1s ease-in-out forwards;
  }

  .text-name:not(:hover) {
    animation: retractName 0.1s ease-in-out forwards;
  }

  @keyframes expandName {
    0% {
      transform: scale(1);
    }
    100% {
      transform: scale(1.2);
      z-index: 1000;
    }
  }

  @keyframes retractName {
    0% {
      transform: scale(1.2);
    }
    100% {
      transform: scale(1);
      z-index: 0;
    }
  }

  .gradient-image:hover {
    animation: rotateAndDissolve 0.5s ease-in-out forwards;
  }

  .gradient-image:not(:hover) {
    animation: revertAnimation 0.5s ease-in-out forwards;
  }

  @keyframes rotateAndDissolve {
    0% {
      transform: rotate(0deg) scale(1);
      opacity: 1;
    }
    50% {
      transform: rotate(180deg) scale(1.1);
      opacity: 0;
    }
    100% {
      transform: rotate(360deg) scale(1.2);
      z-index: 1000;
      opacity: 1;
    }
  }

  @keyframes revertAnimation {
    0% {
      transform: rotate(360deg) scale(1.2);
      z-index: 1000;
      opacity: 1;
    }
    50% {
      transform: rotate(180deg) scale(1.1);
      opacity: 0;
    }
    100% {
      transform: rotate(0deg) scale(1);
      opacity: 1;
    }
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
</style>
