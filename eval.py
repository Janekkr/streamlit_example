def eval(cat, embedding_model, weights):
    transformer = weights.transforms()
    embedding = embedding_model(transformer(cat).unsqueeze(0)).squeeze(0).detach().numpy()
    return embedding