//import React, { useState, useEffect } from 'react';
//import axios from 'axios';

import "./style.css";
import { Frame } from './Frame';

function App() {
 

  /*return (
    <div>
      <h1>Items</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );*/




  return (

    <div>
      <Frame />
    </div>
  );
};

export default App;
/*import React, { useState } from 'react';

function Counter() {
  // 在这里定义了 count 状态变量
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Current count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default Counter;

*/