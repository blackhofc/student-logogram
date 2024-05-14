<script>
  import { onMount } from "svelte";
  import { navigate } from "svelte-routing";

  // Import Utils
  import { loadStudents, logogramSymbols } from "./utils/utils";

  // Import componenets
  import Student from "./Component/Student.svelte";
  import Footer from "./Component/Footer.svelte";
  import PopAbout from "./Component/Popup/About.svelte";
  import SmokeEffect from "./Component/Effects/Smoke.svelte";

  // Variables
  let isAboutVisible = false;
  let selectedStudent = null;

  // Define a function to handle the custom event
  function handleStudentClick(event) {
    // Access the student data from the event detail
    const selectedLogogram = event.detail;
    selectedStudent = selectedLogogram.detail;
    console.log("Student clicked in App:", selectedLogogram);
    logogramSymbols(selectedStudent);

    navigate(`/logogram/${selectedStudent.id}`);
  }

  // On website mounted
  onMount(() => {});
</script>

<div style="display: flex; postion:relative; flex-direction: column;">
  <div class="head-container" style="z-index: 1000;">
    <div
      class="text-title"
      style="text-align: center; font-size: 65px; margin-top: 16px;"
    >
      Student Logogram
    </div>
    <div style="margin-top: 15px; text-align: center;" class="text-sub">
      ¡Visualiza los intereses de 29 estudiantes representados en logogramas del
      lenguaje hetapod!
    </div>
    <a
      class="text-sub"
      style="text-decoration: underline; text-underline-offset: 5px"
      href="https://creativechair.org/stephen-wolfram/"
      target="_blank"
    >
      (Referencia de Inspiración)
    </a>
  </div>

  <div class="logograms-container" style="margin-top: 100px;">
    {#each loadStudents() as student}
      <Student {student} on:studentClicked={handleStudentClick} />
    {/each}
  </div>

  <div
    style="display: flex; position: relative; z-index: 1000; max-height: 150px; bottom:0;"
  >
    <Footer />
  </div>
</div>

<SmokeEffect />

<PopAbout
  visible={isAboutVisible}
  onClose={function () {
    isAboutVisible = !isAboutVisible;
  }}
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

  .logograms-container {
    margin-top: 100px;
    margin-bottom: 100px;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 10px;
    justify-items: center;
  }

  .text-title {
    font-family: "Gotham Light", sans-serif;
    font-size: 50px;
    color: #000000;
  }

  /* 444444 */
  .text-sub {
    font-family: "Gotham Light", sans-serif;
    font-size: 20px;
    color: #000000;
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

  :global(body) {
    background-image: url("/images/background.jpg");
    background-attachment: fixed;
    height: 100%;
    width: 100%;
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
  }
</style>
