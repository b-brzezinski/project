N = 5000
M = 1000
T = 10

u=-1
D=1
values, means, sigma, p_val = schemes.distributions(u,D,M,T,N)


x = np.arange(np.amin(values),np.amax(values),0.01)
fig = go.Figure()

for step in range(100):
    fig.add_trace(
        go.Scatter(
            visible=False,
            name = f'step: {str(step)}',
            x=x,
            y=norm.pdf(x,means[int(step*N/100)],sigma[int(step*N/100)])
        )
    )
fig.data[0].visible = True

steps = []
for i in range(100):
    step = dict(
        method="update",
        args=[{"visible": [False]* 100},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "snapshot: "},
    pad={"t": 100},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show