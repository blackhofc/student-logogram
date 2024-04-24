<script>
  import { onMount } from "svelte";

  // Import Utils
  import {
    loadStudents,
    logogramSymbols,
    describeStudent,
  } from "./utils/utils";

  // Import componenets
  import Student from "./rComponents/Logogram.svelte";
  import Popup from "./rComponents/Popup.svelte";

  // Variables
  let isPopupVisible = false;
  let selectedStudent = null;
  let style = "";
  let students = loadStudents();

  function togglePopup() {
    isPopupVisible = !isPopupVisible;
  }

  // Define a function to handle the custom event
  function handleStudentClick(event) {
    // Access the student data from the event detail
    if (event) {
      const selectedLogogram = event.detail;
      selectedStudent = selectedLogogram.detail;
    }

    students = loadStudents(selectedStudent.id);

    console.log("Student clicked in App:", selectedStudent);
    style = `mask-image: url(${selectedStudent.symbol}); background-image: linear-gradient(to bottom right, ${selectedStudent.gradient});`;
    logogramSymbols(selectedStudent);
  }

  // On website mounted
  onMount(() => {
    selectedStudent = students.find((student) => student.id === 8);
    handleStudentClick();
  });
</script>

<div class="page">
  <div class="row-container">
    <div class="logograms-container">
      {#each students as student}
        <Student {student} on:studentClicked={handleStudentClick} />
      {/each}
    </div>

    <div class="current-logogram-container">
      <div class="gradient-image" {style}></div>
    </div>

    <div class="data-container">
      <div class="text-title" style="font-size: 35px; color: #2E302F; ">
        {selectedStudent?.id}th Logogram
      </div>
      <div class="text-sub" style="color: #2E302F; ">
        {describeStudent(selectedStudent)}
      </div>
    </div>
  </div>
</div>

<Popup
  student={selectedStudent}
  visible={isPopupVisible}
  onClose={togglePopup}
/>

<style>
  .page {
    display: flex;
    position: fixed;
    max-width: 100vw;
    max-height: 100vh;
    height: 100%;
    width: auto;
    flex-direction: row;
    align-items: center;
  }

  .row-container {
    display: flex;
    position: fixed;
    max-width: 100vw;
    max-height: 80vh;
    height: 100%;
    width: auto;
    flex-direction: row;
    align-items: center;
    margin-right: 32px;
  }

  .logograms-container {
    display: flex;
    position: relative;
    width: 100%;
    height: 100%;
    max-width: 25%;
    max-height: auto; /* 75% of the viewport height */
    align-items: center;
    flex-direction: row;
    flex-wrap: wrap;
    overflow-y: auto;
    justify-content: center;
    background-color: #0000008a;
    /*justify-content: space-between; */
  }

  .current-logogram-container {
    display: flex;
    position: relative;
    width: 100%;
    height: 100%;
    margin-left: 32px;
    margin-right: 32px;
  }

  .data-container {
    display: flex;
    position: relative;
    height: 100%;
    width: 100%;
    max-width: 25%;
    max-height: auto;
    flex-direction: column;
    flex-wrap: nowrap;
    overflow-y: auto;
    /*background-color: red;
    justify-content: space-between; */
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
    width: 6px;
  }

  /* Track */
  ::-webkit-scrollbar-track {
    box-shadow: inset 0 0 1px #808080;
    border-radius: 0px;
    background-color: #212224;
  }

  /* Handle */
  ::-webkit-scrollbar-thumb {
    background: #b3b3b3;
    border-radius: 0px;
  }

  /* Handle on hover */
  ::-webkit-scrollbar-thumb:hover {
    background: #808080;
  }
</style>
