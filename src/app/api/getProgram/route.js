import axios from "axios";

export async function POST(req) {
    const { birimId, planTipiKodu } = await req.json();

    try {
        const response = await axios.post(
            "https://obs.itu.edu.tr/public/DersPlan/GetAkademikProgramByBirimIdAndPlanTipi",
            { birimId, planTipiKodu },
            {
                headers: {
                    "User-Agent": "Mozilla/5.0 ...",
                    "Cookie": "your_session_cookie_here",
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            },
        );

        return new Response(JSON.stringify(response.data), {
            status: 200,
            headers: { "Content-Type": "application/json" },
        });
    } catch (error) {
        return new Response(
            JSON.stringify({ error: error.message }),
            { status: 500 }
        );
    }
}
