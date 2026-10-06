// Mobile menu
const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".site-nav");
if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
}

// Fade sections in as they scroll into view
const revealTargets = document.querySelectorAll(".card, .steps li, .tile, .figure, .section-head");
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealTargets.forEach((el) => {
    el.classList.add("reveal");
    observer.observe(el);
  });
}

// Quote form: posts to the form service when one is configured in build.py,
// otherwise opens the visitor's email app with the enquiry filled in.
const form = document.getElementById("quote-form");
if (form) {
  const status = form.querySelector(".form-status");
  const setStatus = (text, kind) => {
    status.textContent = text;
    status.className = "form-status " + kind;
  };

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    let firstInvalid = null;
    form.querySelectorAll("input, textarea").forEach((input) => {
      const bad = !input.checkValidity();
      input.closest(".field").classList.toggle("invalid", bad);
      if (bad && !firstInvalid) firstInvalid = input;
    });
    if (firstInvalid) {
      setStatus("Please fill in your name, a valid email and the project details.", "error");
      firstInvalid.focus();
      return;
    }

    const data = new FormData(form);
    const endpoint = form.dataset.endpoint;
    if (endpoint) {
      try {
        const response = await fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } });
        if (!response.ok) throw new Error(response.statusText);
        form.reset();
        setStatus("Thank you. Your enquiry has been sent and we will be in touch shortly.", "ok");
      } catch (error) {
        setStatus("Sorry, the enquiry could not be sent. Please call or email us instead.", "error");
      }
      return;
    }

    const body = [
      "Name: " + data.get("name"),
      "Email: " + data.get("email"),
      "Phone: " + data.get("phone"),
      "Service: " + data.get("service"),
      "Property type: " + data.get("property"),
      "",
      data.get("message"),
    ].join("\n");
    window.location.href = "mailto:" + form.dataset.email +
      "?subject=" + encodeURIComponent("Quote request: " + data.get("service")) +
      "&body=" + encodeURIComponent(body);
    setStatus("Your email app should now open with the enquiry ready to send.", "ok");
  });
}
