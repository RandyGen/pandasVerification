# データの連続判定を行うソースコード
import pandas as pd
import random


def chk_dataframe_series(df):  # 比較するソースコード
    sorted_df = df.drop_duplicates(subset=['group1', 'group2', 'value']).sort_values(['group1', 'group2', 'value'])
    created_df = sorted_df[(sorted_df.group1 != sorted_df.group1.shift())
                           & (sorted_df.group2 != sorted_df.group2.shift())
                           & (sorted_df.value.diff() != 1)]


if __name__ == '__main__':

    repeat_time = 10  # 繰り返す回数
    cum_execute_time = 0  # 累計処理時間
    dataframe_len = 100  # Dataframeのindexの長さ

    # データ作成
    random.seed(0)
    group1_list = [random.randint(0, 10) for j in range(dataframe_len)]
    random.seed(1)
    group2_list = [random.randint(0, 10) for j in range(dataframe_len)]
    random.seed(2)
    value_list = [random.randint(0, 10) for j in range(dataframe_len)]
    sample_df = pd.DataFrame({'group1': group1_list,
                              'group2': group2_list,
                              'value': value_list})

    chk_dataframe_series(sample_df)

    print('execute complete')
