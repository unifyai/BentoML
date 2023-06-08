from __future__ import annotations

import typing as t
from typing import TYPE_CHECKING

import jax.numpy as jnp
from PIL.Image import Image as PILImage

import bentoml

if TYPE_CHECKING:
    from numpy.typing import NDArray

mnist_runner = bentoml.pytorch.get("pytorch_mnist").to_runner(ivy_transpile=True)

svc = bentoml.Service(name="mnist_flax", runners=[mnist_runner])


@svc.api(input=bentoml.io.Image(), output=bentoml.io.NumpyNdarray())
async def predict(f: PILImage) -> NDArray[t.Any]:
    arr = jnp.array(f) / 255.0
    arr = jnp.expand_dims(arr, (0, 1))
    res = await mnist_runner.async_run(arr)
    print('service output ', res.argmax())
    return res.argmax()
