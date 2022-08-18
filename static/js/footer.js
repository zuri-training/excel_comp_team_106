const footerTemplate = document.createElement('template');

footerTemplate.innerHTML = `
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

footer {
     // position: fixed;
    //bottom: 0;
    width: 100%;
    background-color: #AAC2F2;
    font-family: 'Raleway', sans-serif;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    // padding: 2rem 1rem;
}

footer #xl-sweep-logo {
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

.footer-top ul  {
    display: flex;
    list-style-type: none;
    padding: 1rem 2rem 4rem ;
}

.footer-top li a {
    margin-right: 30px;
    margin-left: 30px;
    text-decoration: none;
    color: #000;
    font-weight: 700;
    font-size: 16px;
    line-height: 24px;
}

.footer-top li a:first-child {
    margin-left: 10px;
} 

hr {
    width: 90%;
    margin: auto;
    border: 1px solid #00256B;
}

.footer-bottom {
    display: flex;
    justify-content: space-between;
    font-family: 'Space Grotesk';
    font-weight: 400;
    font-size: 12px;
    color: #001847;
    line-height: 18px;
    padding: 2rem 0.8rem;
}

.footer-bottom ul {
    display: flex;
    justify-content: space-between;
    list-style-type: none;
}

.footer-bottom li a {
    text-decoration: none;
    margin-left: 10px;
    margin-right: 10px;
    color: #001847;
}
</style>

    <footer>
    {% load static %}
        <div id="xl-sweep-logo">
            <div id="xl-logo">
                <div class="green-logo">
                    <img class="logo" src="{% static 'img/Vectorgreen.png'%}"     class="vectorgreen" alt="">
                </div>
                <div class="blue-logo">
                    <img class="logo" src="{% static 'img/Vectorblue.png'%}"  class="vectorblue" alt="">
                </div>
            </div>
            <div class="sweep">
                <h2>XL SWEEP</h2>
            </div>
        </div>

    
        <div class="footer-top">
            <ul>
                <li><a href="{% url 'Accounts-home' %}" class="index">Home</a></li>
                <li><a href="{% url 'about' %}">About</a></li>
                <li><a href="{% url 'contact' %}">Contact</a></li>
            </ul>
        </div>
        <hr>
        <div class="footer-bottom">
            <ul>
                <li>Terms & Conditions |</li>
                <li><a href="./privacy.html">Privacy Policy |</a></li>
            </ul>
            <p>XL Sweep 2022. All rights reserved.</p>
        </div>
            

    </footer>
`;

class Footer extends HTMLElement {
  constructor() {
   super();
  }

  connectedCallback() {
    const fontAwesome = document.querySelector('link[href*="font-awesome"]');
    const shadowRoot = this.attachShadow({ mode: 'closed' });

     if (fontAwesome) {
       shadowRoot.appendChild(fontAwesome.cloneNode());
   }

     shadowRoot.appendChild(footerTemplate.content);
   }
}

customElements.define('footer-component', Footer);