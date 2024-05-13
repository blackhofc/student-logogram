<!-- Popup.svelte -->
<script>
  import { VARIABLES } from "../../utils/utils.js";

  import Variable from "../Variable.svelte";
  import Container from "../Container.svelte";
  import Music from "../Music.svelte";

  export let visible;
  export let onClose;

  function closePopup(value) {
    onClose();
  }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
{#if visible}
  <div class="popup-overlay" on:click={closePopup}>
    <div class="popup-content" on:click|stopPropagation>
      <div class="head-container">
        <div class="text-title">Student Logogram</div>
        <div style="margin-top: 15px; text-align: center;" class="text-sub">
          Proyecto de visualización de datos inspirado en la película
          "Arrival".Descubre cómo transformamos las respuestas de una encuesta
          en logogramas, capturando intereses y preferencias en un lenguaje
          visual único.
        </div>
        <a
          class="text-sub"
          style=" text-decoration: underline; text-underline-offset: 5px"
          href="https://creativechair.org/stephen-wolfram/"
          target="_blank"
        >
          (Referencia de Inspiración)
        </a>
      </div>

      <div class="variables-container">
        {#each Object.entries(VARIABLES) as [key, variable]}
          <Variable {variable} />

          <div class="row-container">
            <div class="container">
              {#if key === "music_genres"}
                {#each Object.entries(variable.data) as [name, symbol]}
                  <Music {name} v={symbol} />
                {/each}
              {:else}
                {#each Object.entries(variable.data) as [name, symbol]}
                  <Container {name} {symbol} />
                {/each}
              {/if}
            </div>
          </div>
        {/each}
      </div>
    </div>
  </div>
{/if}

<style>
  .popup-overlay {
    z-index: 1500;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.103); /* Semi-black background */
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .popup-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-left: 5%;
    margin-right: 5%;
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: column;
    max-height: 85vh;
    max-width: 85vw;
    overflow-x: auto;
    overflow-y: auto;
  }

  .head-container {
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: column;
    flex-wrap: wrap;
    margin: 15px;
    justify-content: space-between;
  }

  .variables-container {
    display: flex;
    position: relative;
    align-items: start;
    flex-direction: column;
    flex-wrap: wrap;
    padding-left: 32px;
    padding-right: 32px;
    align-items: center;
    width: 100%; /* Occupy the full width of its parent */
  }

  .row-container {
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: row;
    max-width: 100%;
    overflow-x: auto;
  }

  .container {
    display: flex;
    align-items: start;
    height: auto;
    flex-wrap: nowrap; /* Prevent wrapping onto multiple lines */
    flex-direction: row;
    margin-bottom: 8px;
  }

  .logograms-container {
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
    margin: 20px;
  }

  :global(body) {
    background-color: white;
    height: 100vh;
    width: 100%;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
  }

  .text-title {
    font-family: "Gotham Light", sans-serif;
    font-size: 45px;
    color: #444444;
  }

  .text-sub {
    font-family: "Gotham Light", sans-serif;
    font-size: 16px;
    color: #797979;
    margin-left: 4px;
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
