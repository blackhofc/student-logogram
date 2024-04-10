<!-- Ship.svelte -->
<script>
  import { createEventDispatcher } from "svelte";

  export let student;
  const style = `mask-image: url(${student.symbol}); background-image: linear-gradient(to bottom right, ${student.gradient});`;

  const dispatch = createEventDispatcher();

  function handleClick() {
    // Dispatch a custom event with the student data
    dispatch("studentClicked", { detail: student });
  }

  let tooltipText = "Additional information goes here.";

  function handleMouseOver() {
    // You can modify this function to change tooltip text dynamically if needed
    console.log("hover!!", student.name);
    // tooltipText = student.additionalInfo;
  }

  function handleMouseLeave() {
    // Reset tooltip text or perform any other actions when mouse leaves
    console.log("leaved-.-", student.name);
    // tooltipText = ""; // Clear tooltip text
  }

  function handleFocus() {
    // This function mirrors the functionality of handleMouseOver for keyboard focus
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
  <!-- Tooltip -->
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
    border: 1px solid black;
  }

  .gradient-image {
    width: 100%;
    height: 100%;
    -webkit-mask-size: cover;
    mask-position: center;
    mask-repeat: no-repeat;
    mask-size: 100%;
    mask-mode: alpha;
    margin-top: 15px;
    color: transparent;
    background-size: 200% 200%;
    animation: animateGradient 10s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    background-size: 200% 200%;
    background-position: 0% 100%;
    animation-direction: alternate;
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

  .image-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    z-index: 2;
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
