<script>
  import { onMount } from "svelte";

  // Import Utils
  import { VARIABLES, loadStudents, logogramSymbols } from "./utils/utils";

  // Import componenets
  import Student from "./components/Student.svelte";
  import Variable from "./components/Variable.svelte";
  import Container from "./components/Container.svelte";
  import Music from "./components/Music.svelte";
  import Popup from "./components/Popup.svelte";

  // Variables
  let isPopupVisible = false;
  let selectedStudent = null;

  function togglePopup() {
    isPopupVisible = !isPopupVisible;
  }

  // Define a function to handle the custom event
  function handleStudentClick(event) {
    // Access the student data from the event detail
    const selectedLogogram = event.detail;
    selectedStudent = selectedLogogram.detail;
    console.log("Student clicked in App:", selectedLogogram);
    logogramSymbols(selectedStudent);
    togglePopup();
  }

  // On website mounted
  onMount(() => {});
</script>

<div class="head-container">
  <div class="text-title" style="font-size: 65px; margin-top: 32px;">
    Student Logogram
  </div>
  <div style="margin-top: 15px;" class="text-sub">
    La representación en logograma de los intereses de un estudiante en el
    lenguaje alien
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

<div class="logograms-container">
  {#each loadStudents() as student}
    <Student {student} on:studentClicked={handleStudentClick} />
  {/each}
</div>

<Popup
  student={selectedStudent}
  visible={isPopupVisible}
  onClose={togglePopup}
/>

<style>
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
  }

  .row-container {
    display: flex;
    position: relative;
    align-items: center;
    flex-direction: row;
    max-width: 80%;
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
    font-size: 50px;
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
    height: 10px;
    width: 2px;
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
