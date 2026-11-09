"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [attendance, setAttendance] = useState("");
  const [mathematics, setMathematics] = useState("");
  const [science, setScience] = useState("");
  const [english, setEnglish] = useState("");

  const [result, setResult] = useState<any>(null);

  const predictRisk = async () => {
    try {
      const response = await axios.post(
        // "http://127.0.0.1:8000/predict",
        "https://student-intervention-ai-1.onrender.com/predict",
        {
          attendance: Number(attendance),
          mathematics: Number(mathematics),
          science: Number(science),
          english: Number(english),
        }
      );

      setResult(response.data);
    } catch (error) {
      console.log(error);
      alert("Error connecting to backend");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Student Intervention AI</h1>

      <input
        type="number"
        placeholder="Attendance"
        value={attendance}
        onChange={(e) => setAttendance(e.target.value)}
      />

      <br /><br />

      <input
        type="number"
        placeholder="Mathematics"
        value={mathematics}
        onChange={(e) => setMathematics(e.target.value)}
      />

      <br /><br />

      <input
        type="number"
        placeholder="Science"
        value={science}
        onChange={(e) => setScience(e.target.value)}
      />

      <br /><br />

      <input
        type="number"
        placeholder="English"
        value={english}
        onChange={(e) => setEnglish(e.target.value)}
      />

      <br /><br />

      <button onClick={predictRisk}>
        Predict Risk
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Prediction Result</h2>

          <pre>
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}