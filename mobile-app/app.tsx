import React, { useState } from "react";
import { View, TextInput, Button, FlatList, Text } from "react-native";

export default function App() {
  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);
  const [model, setModel] = useState("smart");

  const send = async () => {
    const res = await fetch("https://YOUR_DOMAIN/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ message: msg, model })
    });

    const data = await res.json();

    setChat([...chat,
      { role: "user", text: msg },
      { role: "ai", text: JSON.stringify(data) }
    ]);

    setMsg("");
  };

  return (
    <View style={{ flex: 1, padding: 20, backgroundColor: "#0f172a" }}>
      
      <FlatList
        data={chat}
        renderItem={({ item }) => (
          <Text style={{ color: "white" }}>
            {item.role}: {item.text}
          </Text>
        )}
      />

      <TextInput
        value={msg}
        onChangeText={setMsg}
        style={{ backgroundColor: "#1e293b", color: "white" }}
      />

      <Button title="Send" onPress={send} />
    </View>
  );
}
