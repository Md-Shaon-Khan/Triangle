    fetch('./data.json')   // fetch your JSON file
      .then(response => response.json())  // convert response to JS object
      .then(data => {
        const list = document.getElementById("memberList");

        data.forEach(member => {
          const li = document.createElement("li");
          li.textContent = `ID: ${member.member_id}, Name: ${member.name}, Age: ${member.age}`;
          list.appendChild(li);
        });
      })
      .catch(error => console.error("Error fetching JSON:", error));
