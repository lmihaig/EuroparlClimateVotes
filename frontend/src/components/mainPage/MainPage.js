import React from "react";
import Navbar from "../navbar/navbar";

function MainPage() {
  return (
    <div>
      <Navbar />

      <div class="container-nice m-auto">
        <div class="text-center">
          <svg xmlns="http://www.w3.org/2000/svg" width="150" height="150" fill="currentColor" class="bi bi-brightness-alt-high-fill" viewBox="0 0 16 16">
          <path d="M8 3a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 3zm8 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zm-13.5.5a.5.5 0 0 0 0-1h-2a.5.5 0 0 0 0 1h2zm11.157-6.157a.5.5 0 0 1 0 .707l-1.414 1.414a.5.5 0 1 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm-9.9 2.121a.5.5 0 0 0 .707-.707L3.05 5.343a.5.5 0 1 0-.707.707l1.414 1.414zM8 7a4 4 0 0 0-4 4 .5.5 0 0 0 .5.5h7a.5.5 0 0 0 .5-.5 4 4 0 0 0-4-4z" />
        </svg>
        </div>
        
        <h1 class="text-center m-top--40 f-size-60 ">
          Political Climate
        </h1>
        <p class="text-center">
          FIND OUT THE POLITICAL VIEWS ON THE CLIMATE
        </p>
        <p class="text-center m-top-40">
          How anchored in the current climate issues<br></br>
          is your favorite politician?
        </p>
        <p class="text-center bold">
          If you care about the environment, voting for a<br></br>
          a climate knowledgeable politician is key to a bright future.
        </p>
        <div class="text-center m-top-30">
          <a href="/MembersOfParliament"><button class="research-btn bold">View Our Research</button></a>
        </div>
        
      </div>
    </div>
  );
}

export default MainPage;
