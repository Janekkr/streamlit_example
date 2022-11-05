from zenml.pipelines import pipeline


@pipeline()
def train_model_ppl(load_model, create_dataset, train_model):
    a = load_model()
    b = create_dataset()
    train_model(a[0], a[1], b)


if __name__ == "__main__":
    from steps.load_model import load_model
    from steps.create_dataset import create_dataset
    from steps.train_model import train_model

    pipeline = train_model_ppl(load_model(), create_dataset(), train_model())
    pipeline.run()
