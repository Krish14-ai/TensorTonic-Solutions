import math

def log_loss(y_true, y_pred, eps=1e-15):
    losses = []

    for i in range(len(y_true)):
        p = min(max(y_pred[i], eps), 1 - eps)

        loss = -(y_true[i] * math.log(p) +
                 (1 - y_true[i]) * math.log(1 - p))

        losses.append(loss)

    return losses