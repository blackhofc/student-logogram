<!-- Footer.svelte -->
<div class="footer">
  <div class="container">
    <div class="icons">
      <a
        href="https://github.com/blackhofc/student-logogram"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img src="/images/socials/github.png" alt="Github" class="icon" />
      </a>
      <a
        href="https://www.figma.com/proto/IvTPuLXJyB2YAapTCfqK4X/Student-Logogram---Presentaci%C3%B3n?page-id=0%3A1&node-id=590-634&viewport=263%2C245%2C0.13&t=Mlwez0K8fgqWTuhR-1&scaling=contain&starting-point-node-id=590%3A634"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img
          src="/images/socials/figma.png"
          alt="Figma"
          class="icon"
          style="margin-top:5px"
        />
      </a>
      <a
        href="https://www.linkedin.com/in/bjtoledo/"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img src="/images/socials/linkedin.png" alt="Linkedin" class="icon" />
      </a>
    </div>
  </div>
  <img
    src="/images/socials/utdt.png"
    alt="UTDT"
    class="icon"
    style="margin-left:2px"
  />
</div>

<style>
  .footer {
    background-image: url("/images/footer.png");
    padding: 20px 0;
    text-align: center;
    width: 100%;
    height: 100%;
  }

  .container {
    max-height: 150px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .icons {
    display: flex;
    justify-content: center;
    gap: 100px; /* Adjust the gap as needed */
  }

  .icon {
    transform: scale(0.8); /* Scale the icon to 80% of its original size */
  }
</style>
