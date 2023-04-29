import React, { useState } from 'react';

const haikuAPI = 'https://haiku-api.com/api/random';

const HaikuGenerator = () => {
  const [haiku, setHaiku] = useState('');
  const [prompt, setPrompt] = useState('');

  const generateHaiku = async () => {
    // const response = await fetch(`${haikuAPI}?prompt=${prompt}`);
    // const data = await response.json();
    // setHaiku(data.text);
    setHaiku(
      'sunshine tornado / atmosphere forecast climate / tornado lightning'
    );
  };

  const styles = {
    container: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      marginTop: '50px',
      fontFamily: 'Arial, sans-serif',
    },
    title: {
      fontSize: '24px',
      fontWeight: 'bold',
      marginBottom: '20px',
    },
    input: {
      width: '300px',
      height: '40px',
      borderRadius: '4px',
      border: '1px solid gray',
      padding: '10px',
      fontSize: '16px',
      marginBottom: '20px',
    },
    button: {
      width: '200px',
      height: '40px',
      backgroundColor: 'blue',
      color: 'white',
      borderRadius: '4px',
      border: 'none',
      fontSize: '16px',
      cursor: 'pointer',
      marginBottom: '20px',
    },
    haiku: {
      fontSize: '20px',
      fontStyle: 'italic',
      textAlign: 'center',
      maxWidth: '500px',
    },
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>AI Haiku Generator</h1>
      <label htmlFor='promptInput'>Enter a poem prompt:</label>
      <br />
      <input
        id='promptInput'
        type='text'
        style={styles.input}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <br />
      <button onClick={generateHaiku} style={styles.button}>
        Generate Haiku
      </button>
      <p style={styles.haiku}>{haiku}</p>
    </div>
  );
};

export default HaikuGenerator;
