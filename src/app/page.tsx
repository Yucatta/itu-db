"use client";
import Image from "next/image";
import axios from "axios";
import { useEffect } from "react";

export default function Home() {
  const BaseService = axios.create({
    baseURL: "https://obs.itu.edu.tr",
    timeout: 1000,
  });

  useEffect(() => {
    async function getProgram() {
      const res = await fetch("/api/getProgram", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ birimId: "3", planTipiKodu: "lisans" }),
      });

      const data = await res.json();
      console.log(data);
    }
    getProgram();
  }, []);

  return (
    <div>
      <div>
        <div>
          <div></div>
        </div>
      </div>
    </div>
  );
}
