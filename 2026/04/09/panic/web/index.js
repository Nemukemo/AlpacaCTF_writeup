import fastify from "fastify";

const index = `
<style>
  @keyframes fadeout {
    from { opacity: 0.7; transform: scale(1.1); }
    to { opacity: 1; transform: scale(0); }
  }
</style>
<script>
  let i = 0;
  const f = window.onload = () => {
    const e = document.createElement("marquee");
    e.textContent = ["🦙", "🐫"][(Math.random() > 0.97) | 0];
    e.setAttribute("scrollamount", "24");
    e.style.fontSize = \`\${++i}em\`;
    e.style.position = "absolute";
    e.style.animation = \`fadeout \${30 + i}s ease-in forwards\`;
    document.body.appendChild(e);
    if (document.body.children.length > 30) {
      document.body.firstChild.remove();
    }
    setTimeout(f, 50*i);
  };
</script>
`.trim();

fastify()
  // Accept all requests
  .all("/*", (req, reply) => reply.type("text/html; charset=utf-8").send(index))
  // Panic!
  .setErrorHandler((error) => process.env.FLAG)
  // Run the server
  .listen({ port: 3000, host: "0.0.0.0" });
