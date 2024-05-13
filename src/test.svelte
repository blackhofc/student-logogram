<script>
  import { onMount } from "svelte";
  import SmokeEffect from "./Component/Effects/Smoke.svelte";

  let style_1 = `mask-image: url(./images/logograms/8.png); background-image: linear-gradient(to bottom right, black, black);`;
  let style_2 = `mask-image: url(./images/logograms/8.png); background-image: linear-gradient(to bottom right, red, blue); `;

  let isHovered = false;

  function toggleHover() {
    isHovered = !isHovered;
  }

  function stopSmokeEffect() {
    // Optionally clear any remaining smoke after stopping
    // smokeEffect.step(1000);
  }

  // On website mounted
  onMount(() => {});
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
  class="card-container"
  on:mouseenter={toggleHover}
  on:mouseleave={toggleHover}
>
  <div class="gradient-image" style={isHovered ? style_2 : style_1}></div>
  <div class="gradient-image-2" style={isHovered ? style_2 : style_1}></div>
</div>
<div class="nebxula"></div>
<div class="glowing-gradient"></div>
<div class="current-logogram-container"></div>
<SmokeEffect />

<style>
  :global(body) {
    background-image: url("./images/back.jpg");
    height: 100%;
    width: 100%;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
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
    background-position: 0% 100%;
    cursor: pointer;
    transition:
      background-image 0.5s ease,
      mask-image 0.5s ease,
      transform 0.5s ease;
  }

  .gradient-image:hover {
    background-size: 100% 100%;
    transform: rotate(360deg) scale(1.2);
  }

  .gradient-image-2 {
    width: 350px;
    height: 350px;
    mask-size: 100%;
    cursor: pointer;
  }

  .gradient-image-2:hover {
    animation: rotateAndDissolve 0.5s ease-in-out forwards;
  }

  .gradient-image-2:not(:hover) {
    animation: revertAnimation 0.5s ease-in-out forwards;
  }

  @keyframes rotateAndDissolve {
    0% {
      mask-image: url(./images/logograms/8.png);
      background-image: linear-gradient(to bottom right, black, black);
      transform: rotate(0deg) scale(1);
      opacity: 1;
    }
    50% {
      mask-image: url(./images/logograms/8.png);
      background-image: linear-gradient(to bottom right, black, black);
      transform: rotate(180deg) scale(1.1);
      opacity: 0;
    }
    100% {
      mask-image: url(./images/logograms/8.png);
      background-image: linear-gradient(to bottom right, red, blue);
      transform: rotate(360deg) scale(1.2);
      z-index: 1000;
      opacity: 1;
    }
  }

  @keyframes revertAnimation {
    0% {
      mask-image: url(./images/logograms/8.png);
      background-image: linear-gradient(to bottom right, red, blue);
      transform: rotate(360deg) scale(1.2);
      z-index: 1000;
      opacity: 1;
    }
    50% {
      mask-image: url(./images/logograms/8.png);
      background-image: linear-gradient(to bottom right, black, black);
      transform: rotate(180deg) scale(1.1);
      opacity: 0;
    }
    100% {
      mask-image: url(./images/logograms/8.png);
      background-image: linear-gradient(to bottom right, black, black);
      transform: rotate(0deg) scale(1);
      opacity: 1;
    }
  }

  .nebulas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(
      255,
      255,
      255,
      0.5
    ); /* Ajusta la transparencia aquí */
    backdrop-filter: blur(2px); /* Ajusta el nivel de desenfoque aquí */
    z-index: 998; /* Asegúrate de que esté debajo del elemento con hover */
    pointer-events: none; /* Permite hacer clic a través de la neblina */
  }

  .glowing-gradient {
    background: linear-gradient(135deg, #ff00ff, #00ffff);
    background-size: 400% 400%;
    animation: glowing 8s ease infinite;
    height: 100px;
    width: 200px;
  }

  @keyframes glowing {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }

  .current-logogram-container {
    width: 200px;
    height: 200px;
    margin-left: 50px;
    background-color: blue;
    position: relative;
    animation: allAnimations 5s infinite alternate ease-in-out;
  }

  @keyframes allAnimations {
    0% {
      transform: translateX(-5px) scale(1) rotate(-4deg);
    }
    50% {
      transform: translateX(5px) scale(1.05) rotate(2deg);
    }
    100% {
      transform: translateX(-5px) scale(1) rotate(-2deg);
    }
  }
</style>
