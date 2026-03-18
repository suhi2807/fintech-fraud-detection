async function buy(user, product, amount) {

    // 🔄 Show loading
    alert("Processing payment... ⏳");

    try {
        let response = await fetch(
            `http://127.0.0.1:8000/buy?user_id=${user}&product_id=${product}&amount=${amount}`
        );

        // ❌ If server error
        if (!response.ok) {
            throw new Error("Server error");
        }

        let data = await response.json();

        // ✅ SUCCESS
        if (data.status === "success") {
            alert(`✅ Payment Successful!\n\n🤖 AI Insight:\n${data.ai}`);
        }

        // ⚠ SUSPICIOUS
        else if (data.status === "suspicious") {
            alert(`⚠ Suspicious Transaction!\n\n👉 Please verify OTP.\n\n🤖 AI Insight:\n${data.ai}`);
        }

        // ❌ FRAUD
        else if (data.status === "fraud") {
            alert(`❌ Fraud Detected!\n\n🚫 Transaction Blocked.\n\n🤖 AI Insight:\n${data.ai}`);
        }

        // ⚠ UNKNOWN RESPONSE
        else {
            alert(`⚠ Unexpected response:\n${data.message}`);
        }

    } catch (error) {
        console.error(error);
        alert("❌ Backend not connected!\n\n👉 Make sure FastAPI server is running.");
    }
}