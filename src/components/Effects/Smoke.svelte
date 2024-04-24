<script>
  import { onMount } from "svelte";
  import SmokeMachine from "@bijection/smoke";
  let canvas;
  let smokeMachine;

  onMount(() => {
    const ctx = canvas.getContext("2d");
    smokeMachine = SmokeMachine(ctx);

    // Set pre-draw callback to adjust globalAlpha for smoother transparency
    smokeMachine.setPreDrawCallback(function (deltatime, particles) {
      ctx.globalAlpha = 1; // Adjust the global alpha for smoother transparency
    });

    // Start the smoke effect
    smokeMachine.start();

    // Continuously add particles to the smoke effect
    setInterval(function () {
      smokeMachine.addsmoke(
        Math.random() * canvas.width, // Random x position within canvas width
        Math.random() * canvas.height, // Random y position within canvas height
        2, // Number of particles to add
        {
          minVx: -0.02, // Adjust minimum x velocity
          maxVx: 0.02, // Adjust maximum x velocity
          minVy: -0.02, // Adjust minimum y velocity
          maxVy: -0.01, // Adjust maximum y velocity
          minScale: 10, // Adjust minimum particle scale
          maxScale: 1, // Adjust maximum particle scale
        }
      );
    }, 100); // Adjust the interval as needed
    return () => {
      //party.stop();
    };
  });
</script>

<canvas class="canvas" bind:this={canvas}></canvas>

<style>
  .canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 900; /* Asegúrate de que esté debajo del elemento con hover */
    pointer-events: none; /* Permite hacer clic a través de la neblina */
    backdrop-filter: blur(2px); /*Ajusta el nivel de desenfoque aquí */
  }
</style>
