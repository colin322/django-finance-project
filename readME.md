# Installatie

### Vereisten

Python 3.8+

### Stappen om te installeren

1. **Clone de repository**:

    ```bash
    git clone https://github.com/your-username/finance-tracker.git
    cd finance-tracker
    ```

2. **Maak een virtuele omgeving aan (optioneel maar aanbevolen)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Voor Mac/Linux
    venv\Scripts\activate     # Voor Windows
    ```

3. **Installeer de benodigde Python-pakketten**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Voer de migraties uit om de database in te stellen**:

    ```bash
    python manage.py migrate
    ```

5. **Start de ontwikkelserver**:

    ```bash
    python manage.py runserver
    ```

6. Ga naar [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in je webbrowser.

---

## Gebruik

1. Registreer een account of log in als je al een account hebt.
2. Vul je persoonlijke financiële gegevens in, zoals maandinkomen, uitgaven en spaargeld.
3. Stel doelen in en houd je voortgang bij.
4. Bekijk de rapporten om inzicht te krijgen in je financiële situatie.
