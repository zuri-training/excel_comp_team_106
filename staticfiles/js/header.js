const headerTemplate = document.createElement("template");

headerTemplate.innerHTML = `
<style>
* {
    margin: 0;
}


html, body{
    scroll-behavior: smooth;
    margin: 0;
    padding: 0;
    max-width: 100%;
    min-height: 100vh;
    max-height: 100vh;
}

#navbar {
    background-color: #fff;
    font-family: 'Raleway', sans-serif;
    display: flex;
    justify-content: space-between;
    padding: 2rem 3rem;
}

#xl-sweep-logo {
    display: flex;
    align-items: left;
    justify-content: left;
}

#xl-logo {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    position: relative;
}

.green-logo {
    position: absolute;
    top: -35%;
    left: -6%;
}

.logo {
    height: 30px;
    margin-right: 10px;
}

.sweep {
    font-size: 20px;
    font-weight: 800;
    color: #003DB1;
    line-height: 23px;
}

ul {
    display: flex;
    list-style-type: none;
}

li a {
    margin-right: 20px;
    margin-left: 20px;
    text-decoration: none;
    color: #000;
    font-weight: 700;
    font-size: 16px;
    line-height: 24px;

}

.nav-btn button {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 400;
    font-size: 16px;
    line-height: 20px;
    letter-spacing: 0.1px;
    border-radius: 5px;
    margin-right: 15px;
    cursor:pointer;
}

.sign-in {
    background-color: #fff;
    color: #003DB1;
    border: 1px solid #003DB1;
    
}

.sign-up {
    background-color: #003DB1;
    color: #fff;
    border: 1px solid #003DB1;
}

</style>

    <header>
       {% load static %}
        <nav id="navbar">
            <div id="xl-sweep-logo">
                <div id="xl-logo">
                    <div class="green-logo">
                        <img class="logo" src="{% static 'img/Vector.png'%}"     class="vectorgreen" alt="">
                    </div>
                    <div class="blue-logo">
                        <img class="logo" src="{% static 'img/Vectorblue.png'%}"  class="vectorblue" alt="">
                    </div>
                </div>
                <div class="sweep">
                    <h2>XL SWEEP</h2>
                </div>
            </div>
            <div class="nav-links">
                <ul>
                    <li><a href="{% url 'Accounts-home' %}>Home</a></li>
                    <li><a href="{% url 'about' %}">About</a></li>
                    <li><a href="{% url 'contact' %}">Contact</a></li>
                </ul>
            </div>
            <div class="nav-btn">
                <a href= "{% url 'login' %}"><button class="sign-in">Sign In</button></a>
            </div>
        </nav>
</header>
`;
class Header extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const shadowRoot = this.attachShadow({ mode: "closed" });

    shadowRoot.appendChild(headerTemplate.content);
  }
}


customElements.define('header-component', Header);