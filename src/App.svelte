<script>
  import { Router, Route } from "svelte-routing";
  import MainPage from "./Main.svelte";
  import LogogramPage from "./Logogram.svelte";
</script>

<Router>
  <Route path="/" component={MainPage} />
  <Route path="/logogram/:id" component={LogogramPage} />
  <!-- Define other routes as needed -->
  <Route component={MainPage} />
  <!-- This will act as the default route -->
</Router>
