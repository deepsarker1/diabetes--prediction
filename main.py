import os
import streamlit as st
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.types import StructType, StructField, FloatType, IntegerType
import findspark


findspark.init()
spark = SparkSession.builder.appName("ClassificationwithSpark").getOrCreate()

model = LogisticRegressionModel.load("trained_model")


def diabetes_prediction(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi,
                            diabetes_pedigree_function, age):
    try:    
        data = [
            (
                int(pregnancies),
                int(glucose),
                int(blood_pressure),
                int(skin_thickness),
                int(insulin),
                float(bmi),
                float(diabetes_pedigree_function),
                int(age),
            )
        ]
    except Exception as e:
        print("=============================================================================")
        print(e)
        print("=============================================================================")
        return "Invalid Input"
    schema = StructType(
        [
            StructField("Pregnancies", IntegerType(), True),
            StructField("Glucose", IntegerType(), True),
            StructField("BloodPressure", IntegerType(), True),
            StructField("SkinThickness", IntegerType(), True),
            StructField("Insulin", IntegerType(), True),
            StructField("BMI", FloatType(), True),
            StructField("DiabetesPedigreeFunction", FloatType(), True),
            StructField("Age", IntegerType(), True),
        ]
    )

    single_row_df = spark.createDataFrame(data, schema)

    vector_assembler = VectorAssembler(
        inputCols=[
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age",
        ],
        outputCol="features",
    )

    single_row_df = vector_assembler.transform(single_row_df)

    prediction = model.transform(single_row_df)

    result = prediction.select("features", "rawPrediction", "probability", "prediction").rdd.flatMap(lambda x: x).collect()
    if result[-1] == 0.0:
        return "NO"
    else:
        return "YES"

def main():
    st.title("Diabetes Prediction Web App")

    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin Level")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the Person")

    diagnosis = ""

    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction(Pregnancies, Glucose, BloodPressure, SkinThickness,
                                            Insulin, BMI, DiabetesPedigreeFunction, Age)

    st.success(diagnosis)


if __name__ == "__main__":
    main()
