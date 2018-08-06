import * as React from "react";
import {BrowserRouter} from "react-router-dom";

class App extends React.Component {
  public render() {
    return (
      <BrowserRouter>
        <div className="App">Nom nom...</div>
      </BrowserRouter>
    );
  }
}

export default App;
