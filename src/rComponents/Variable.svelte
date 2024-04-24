<!-- Variable.svelte -->
<script>
  export let variable;
</script>

<div class="variable-container">
  <div class="flex-box">
    <div class="text-title">{variable.title}:</div>
    <div style="margin-top: 0px;" class="text-sub">
      {variable.description}
    </div>
  </div>
</div>

<style>
  .variable-container {
    margin-left: 6px;
    display: flex;
    position: relative;
    justify-content: space-between;
  }

  .flex-box {
    margin-top: 16px;
    display: flex;
    position: relative;
    flex-direction: row;
    align-items: baseline;
  }

  .text-title {
    font-family: "Gotham Light", sans-serif;
    font-size: 24px;
    color: #444444;
    text-align: left;
    white-space: nowrap;
  }

  .text-sub {
    font-family: "Gotham Light", sans-serif;
    font-size: 18px;
    color: #797979;
    text-align: left;
    white-space: nowrap;
    margin-left: 5px;
  }
</style>
