# small helper: create a simple matplotlib chart and return bytes
import io
import matplotlib.pyplot as plt

def plot_weights(dates, weights):
    fig, ax = plt.subplots()
    ax.plot(dates, weights, marker='o')
    ax.set_title("Weight over time")
    ax.set_ylabel("Weight (kg)")
    ax.set_xlabel("Date")
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig)
    return buf  # flask.send_file can return this buffer