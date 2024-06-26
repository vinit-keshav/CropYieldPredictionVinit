{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eecf2850-7244-4ad0-8bfc-e3babe325d4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "04177f3b-4d81-4af0-8621-845573d42eb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('crop_yield.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9b8bed60-232e-43e0-8186-d3cb466e5f7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Crop</th>\n",
       "      <th>Crop_Year</th>\n",
       "      <th>Season</th>\n",
       "      <th>State</th>\n",
       "      <th>Area</th>\n",
       "      <th>Production</th>\n",
       "      <th>Annual_Rainfall</th>\n",
       "      <th>Fertilizer</th>\n",
       "      <th>Pesticide</th>\n",
       "      <th>Yield</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Arecanut</td>\n",
       "      <td>1997</td>\n",
       "      <td>Whole Year</td>\n",
       "      <td>Assam</td>\n",
       "      <td>73814.0</td>\n",
       "      <td>56708</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>7024878.38</td>\n",
       "      <td>22882.34</td>\n",
       "      <td>0.796087</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Arhar/Tur</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>6637.0</td>\n",
       "      <td>4685</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>631643.29</td>\n",
       "      <td>2057.47</td>\n",
       "      <td>0.710435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Castor seed</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>796.0</td>\n",
       "      <td>22</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>75755.32</td>\n",
       "      <td>246.76</td>\n",
       "      <td>0.238333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Coconut</td>\n",
       "      <td>1997</td>\n",
       "      <td>Whole Year</td>\n",
       "      <td>Assam</td>\n",
       "      <td>19656.0</td>\n",
       "      <td>126905000</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>1870661.52</td>\n",
       "      <td>6093.36</td>\n",
       "      <td>5238.051739</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Cotton(lint)</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>1739.0</td>\n",
       "      <td>794</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>165500.63</td>\n",
       "      <td>539.09</td>\n",
       "      <td>0.420909</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Dry chillies</td>\n",
       "      <td>1997</td>\n",
       "      <td>Whole Year</td>\n",
       "      <td>Assam</td>\n",
       "      <td>13587.0</td>\n",
       "      <td>9073</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>1293074.79</td>\n",
       "      <td>4211.97</td>\n",
       "      <td>0.643636</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Gram</td>\n",
       "      <td>1997</td>\n",
       "      <td>Rabi</td>\n",
       "      <td>Assam</td>\n",
       "      <td>2979.0</td>\n",
       "      <td>1507</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>283511.43</td>\n",
       "      <td>923.49</td>\n",
       "      <td>0.465455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Jute</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>94520.0</td>\n",
       "      <td>904095</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>8995468.40</td>\n",
       "      <td>29301.20</td>\n",
       "      <td>9.919565</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Linseed</td>\n",
       "      <td>1997</td>\n",
       "      <td>Rabi</td>\n",
       "      <td>Assam</td>\n",
       "      <td>10098.0</td>\n",
       "      <td>5158</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>961026.66</td>\n",
       "      <td>3130.38</td>\n",
       "      <td>0.461364</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Maize</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>19216.0</td>\n",
       "      <td>14721</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>1828786.72</td>\n",
       "      <td>5956.96</td>\n",
       "      <td>0.615652</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Crop  Crop_Year       Season  State     Area  Production  \\\n",
       "0      Arecanut       1997  Whole Year   Assam  73814.0       56708   \n",
       "1     Arhar/Tur       1997  Kharif       Assam   6637.0        4685   \n",
       "2   Castor seed       1997  Kharif       Assam    796.0          22   \n",
       "3      Coconut        1997  Whole Year   Assam  19656.0   126905000   \n",
       "4  Cotton(lint)       1997  Kharif       Assam   1739.0         794   \n",
       "5  Dry chillies       1997  Whole Year   Assam  13587.0        9073   \n",
       "6          Gram       1997  Rabi         Assam   2979.0        1507   \n",
       "7          Jute       1997  Kharif       Assam  94520.0      904095   \n",
       "8       Linseed       1997  Rabi         Assam  10098.0        5158   \n",
       "9         Maize       1997  Kharif       Assam  19216.0       14721   \n",
       "\n",
       "   Annual_Rainfall  Fertilizer  Pesticide        Yield  \n",
       "0           2051.4  7024878.38   22882.34     0.796087  \n",
       "1           2051.4   631643.29    2057.47     0.710435  \n",
       "2           2051.4    75755.32     246.76     0.238333  \n",
       "3           2051.4  1870661.52    6093.36  5238.051739  \n",
       "4           2051.4   165500.63     539.09     0.420909  \n",
       "5           2051.4  1293074.79    4211.97     0.643636  \n",
       "6           2051.4   283511.43     923.49     0.465455  \n",
       "7           2051.4  8995468.40   29301.20     9.919565  \n",
       "8           2051.4   961026.66    3130.38     0.461364  \n",
       "9           2051.4  1828786.72    5956.96     0.615652  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ac06a9d-c697-41e1-ae0e-406fca145aaa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Crop               0\n",
       "Crop_Year          0\n",
       "Season             0\n",
       "State              0\n",
       "Area               0\n",
       "Production         0\n",
       "Annual_Rainfall    0\n",
       "Fertilizer         0\n",
       "Pesticide          0\n",
       "Yield              0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4f20bb7c-cc41-4331-8fe9-9fc05bf5c8db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        False\n",
       "1        False\n",
       "2        False\n",
       "3        False\n",
       "4        False\n",
       "         ...  \n",
       "19684    False\n",
       "19685    False\n",
       "19686    False\n",
       "19687    False\n",
       "19688    False\n",
       "Length: 19689, dtype: bool"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "34a690bf-c066-45ef-8dfd-9c1ce999d0be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        False\n",
       "1        False\n",
       "2        False\n",
       "3        False\n",
       "4        False\n",
       "         ...  \n",
       "19684     True\n",
       "19685     True\n",
       "19686     True\n",
       "19687     True\n",
       "19688     True\n",
       "Length: 19689, dtype: bool"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated('Crop')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b61b7fda-9323-49dc-8e8a-b95520f9233d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fffe4dad-4fbe-4728-885c-48b70e88b405",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.boxplot(df['Crop'])\n",
    "# sns.boxplot(df['Crop_Year'])\n",
    "# sns.boxplot(df['Season'])\n",
    "# sns.boxplot(df['State'])\n",
    "# sns.boxplot(df['Area'])\n",
    "# sns.boxplot(df['Production'])\n",
    "# sns.boxplot(df['Annual_Rainfall'])\n",
    "# sns.boxplot(df['Fertilizer'])\n",
    "# sns.boxplot(df['Pesticide'])\n",
    "# sns.boxplot(df['Yield'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0ab43c4d-f7ab-422a-9abb-b77b287b953a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\vinit\\AppData\\Local\\Temp\\ipykernel_11828\\1930570014.py:2: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(df['Season'])\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "could not convert string to float: 'Whole Year '",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[14], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m plt\u001b[38;5;241m.\u001b[39msubplot(\u001b[38;5;241m1\u001b[39m,\u001b[38;5;241m2\u001b[39m,\u001b[38;5;241m1\u001b[39m)\n\u001b[1;32m----> 2\u001b[0m \u001b[43msns\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdistplot\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdf\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mSeason\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\seaborn\\distributions.py:2443\u001b[0m, in \u001b[0;36mdistplot\u001b[1;34m(a, bins, hist, kde, rug, fit, hist_kws, kde_kws, rug_kws, fit_kws, color, vertical, norm_hist, axlabel, label, ax, x)\u001b[0m\n\u001b[0;32m   2440\u001b[0m     a \u001b[38;5;241m=\u001b[39m x\n\u001b[0;32m   2442\u001b[0m \u001b[38;5;66;03m# Make a a 1-d float array\u001b[39;00m\n\u001b[1;32m-> 2443\u001b[0m a \u001b[38;5;241m=\u001b[39m \u001b[43mnp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43masarray\u001b[49m\u001b[43m(\u001b[49m\u001b[43ma\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mfloat\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m   2444\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m a\u001b[38;5;241m.\u001b[39mndim \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m1\u001b[39m:\n\u001b[0;32m   2445\u001b[0m     a \u001b[38;5;241m=\u001b[39m a\u001b[38;5;241m.\u001b[39msqueeze()\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\pandas\\core\\series.py:917\u001b[0m, in \u001b[0;36mSeries.__array__\u001b[1;34m(self, dtype)\u001b[0m\n\u001b[0;32m    870\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    871\u001b[0m \u001b[38;5;124;03mReturn the values as a NumPy array.\u001b[39;00m\n\u001b[0;32m    872\u001b[0m \n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    914\u001b[0m \u001b[38;5;124;03m      dtype='datetime64[ns]')\u001b[39;00m\n\u001b[0;32m    915\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    916\u001b[0m values \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_values\n\u001b[1;32m--> 917\u001b[0m arr \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39masarray(values, dtype\u001b[38;5;241m=\u001b[39mdtype)\n\u001b[0;32m    918\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m using_copy_on_write() \u001b[38;5;129;01mand\u001b[39;00m astype_is_view(values\u001b[38;5;241m.\u001b[39mdtype, arr\u001b[38;5;241m.\u001b[39mdtype):\n\u001b[0;32m    919\u001b[0m     arr \u001b[38;5;241m=\u001b[39m arr\u001b[38;5;241m.\u001b[39mview()\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to float: 'Whole Year '"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAASAAAAGiCAYAAABH+xtTAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8g+/7EAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAYvklEQVR4nO3cb2yV9f3/8VdbOKcYacF1PS3sYAMG/0Nnka4gIS5nNtHUcWOxE0M74p+pnVFONqEiVEQpc4w1kSKxU/GGjjqjxkhTp52NUbuQFJroBAwWbWd2DjSOc1iRFno+3xv7cfzVtspV275beD6S60Y/uz7nend6np5/PSnOOScAMJBqPQCA8xcBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJgxnOA3n33XZWUlGjGjBlKSUnRa6+99p17mpubdc0118jv9+uSSy7Rzp07hzEqgHON5wB1d3dr/vz5qq2tPavzDx8+rJtuuknXX3+92tra9MADD+iOO+7Qm2++6XlYAOeWlO/zx6gpKSl69dVXtWzZsiHPWb16tXbv3q2PPvooufbLX/5Sx44dU2Nj43AvDeAcMGm0L9DS0qJQKNRvrbi4WA888MCQe3p6etTT05P8OZFI6Msvv9QPfvADpaSkjNaoAIbgnNPx48c1Y8YMpaaO3EvHox6gSCSiQCDQby0QCCgej+urr77SlClTBuyprq7Whg0bRns0AB51dnbqRz/60Yjd3qgHaDgqKysVDoeTP8diMc2aNUudnZ3KyMgwnAw4P8XjcQWDQU2dOnVEb3fUA5STk6NoNNpvLRqNKiMjY9BHP5Lk9/vl9/sHrGdkZBAgwNBIvwQy6p8DKioqUlNTU7+1t956S0VFRaN9aQDjnOcA/fe//1VbW5va2tok/e9t9ra2NnV0dEj639OnsrKy5Pl333232tvb9eCDD+rAgQPavn27XnrpJa1atWpkfgMAE5fz6J133nGSBhzl5eXOOefKy8vd0qVLB+zJz893Pp/PzZ492z333HOerhmLxZwkF4vFvI4LYASM1n3we30OaKzE43FlZmYqFovxGhBgYLTug/wtGAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMDCtAtbW1ysvLU3p6ugoLC7Vnz55vPb+mpkaXXnqppkyZomAwqFWrVunkyZPDGhjAucNzgOrr6xUOh1VVVaW9e/dq/vz5Ki4u1pEjRwY9/8UXX9SaNWtUVVWl/fv365lnnlF9fb0eeuih7z08gInNc4C2bt2qO++8UytXrtQVV1yhHTt26IILLtCzzz476PkffPCBFi9erOXLlysvL0833HCDbr311u981ATg3OcpQL29vWptbVUoFPr6BlJTFQqF1NLSMuieRYsWqbW1NRmc9vZ2NTQ06MYbbxzyOj09PYrH4/0OAOeeSV5O7urqUl9fnwKBQL/1QCCgAwcODLpn+fLl6urq0nXXXSfnnE6fPq277777W5+CVVdXa8OGDV5GAzABjfq7YM3Nzdq0aZO2b9+uvXv36pVXXtHu3bu1cePGIfdUVlYqFoslj87OztEeE4ABT4+AsrKylJaWpmg02m89Go0qJydn0D3r1q3TihUrdMcdd0iSrr76anV3d+uuu+7S2rVrlZo6sIF+v19+v9/LaAAmIE+PgHw+nwoKCtTU1JRcSyQSampqUlFR0aB7Tpw4MSAyaWlpkiTnnNd5AZxDPD0CkqRwOKzy8nItWLBACxcuVE1Njbq7u7Vy5UpJUllZmWbOnKnq6mpJUklJibZu3aof//jHKiws1KFDh7Ru3TqVlJQkQwTg/OQ5QKWlpTp69KjWr1+vSCSi/Px8NTY2Jl+Y7ujo6PeI5+GHH1ZKSooefvhhffHFF/rhD3+okpISPf744yP3WwCYkFLcBHgeFI/HlZmZqVgspoyMDOtxgPPOaN0H+VswAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJgZVoBqa2uVl5en9PR0FRYWas+ePd96/rFjx1RRUaHc3Fz5/X7NnTtXDQ0NwxoYwLljktcN9fX1CofD2rFjhwoLC1VTU6Pi4mIdPHhQ2dnZA87v7e3Vz372M2VnZ+vll1/WzJkz9fnnn2vatGkjMT+ACSzFOee8bCgsLNS1116rbdu2SZISiYSCwaDuu+8+rVmzZsD5O3bs0B/+8AcdOHBAkydPHtaQ8XhcmZmZisViysjIGNZtABi+0boPenoK1tvbq9bWVoVCoa9vIDVVoVBILS0tg+55/fXXVVRUpIqKCgUCAV111VXatGmT+vr6hrxOT0+P4vF4vwPAucdTgLq6utTX16dAINBvPRAIKBKJDLqnvb1dL7/8svr6+tTQ0KB169bpj3/8ox577LEhr1NdXa3MzMzkEQwGvYwJYIIY9XfBEomEsrOz9fTTT6ugoEClpaVau3atduzYMeSeyspKxWKx5NHZ2TnaYwIw4OlF6KysLKWlpSkajfZbj0ajysnJGXRPbm6uJk+erLS0tOTa5Zdfrkgkot7eXvl8vgF7/H6//H6/l9EATECeHgH5fD4VFBSoqakpuZZIJNTU1KSioqJB9yxevFiHDh1SIpFIrn3yySfKzc0dND4Azh+en4KFw2HV1dXp+eef1/79+3XPPfeou7tbK1eulCSVlZWpsrIyef4999yjL7/8Uvfff78++eQT7d69W5s2bVJFRcXI/RYAJiTPnwMqLS3V0aNHtX79ekUiEeXn56uxsTH5wnRHR4dSU7/uWjAY1JtvvqlVq1Zp3rx5mjlzpu6//36tXr165H4LABOS588BWeBzQICtcfE5IAAYSQQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzAwrQLW1tcrLy1N6eroKCwu1Z8+es9q3a9cupaSkaNmyZcO5LIBzjOcA1dfXKxwOq6qqSnv37tX8+fNVXFysI0eOfOu+zz77TL/97W+1ZMmSYQ8L4NziOUBbt27VnXfeqZUrV+qKK67Qjh07dMEFF+jZZ58dck9fX59uu+02bdiwQbNnz/7Oa/T09Cgej/c7AJx7PAWot7dXra2tCoVCX99AaqpCoZBaWlqG3Pfoo48qOztbt99++1ldp7q6WpmZmckjGAx6GRPABOEpQF1dXerr61MgEOi3HggEFIlEBt3z3nvv6ZlnnlFdXd1ZX6eyslKxWCx5dHZ2ehkTwAQxaTRv/Pjx41qxYoXq6uqUlZV11vv8fr/8fv8oTgZgPPAUoKysLKWlpSkajfZbj0ajysnJGXD+p59+qs8++0wlJSXJtUQi8b8LT5qkgwcPas6cOcOZG8A5wNNTMJ/Pp4KCAjU1NSXXEomEmpqaVFRUNOD8yy67TB9++KHa2tqSx80336zrr79ebW1tvLYDnOc8PwULh8MqLy/XggULtHDhQtXU1Ki7u1srV66UJJWVlWnmzJmqrq5Wenq6rrrqqn77p02bJkkD1gGcfzwHqLS0VEePHtX69esViUSUn5+vxsbG5AvTHR0dSk3lA9YAvluKc85ZD/Fd4vG4MjMzFYvFlJGRYT0OcN4ZrfsgD1UAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYGZYAaqtrVVeXp7S09NVWFioPXv2DHluXV2dlixZounTp2v69OkKhULfej6A84fnANXX1yscDquqqkp79+7V/PnzVVxcrCNHjgx6fnNzs2699Va98847amlpUTAY1A033KAvvvjiew8PYGJLcc45LxsKCwt17bXXatu2bZKkRCKhYDCo++67T2vWrPnO/X19fZo+fbq2bdumsrKyQc/p6elRT09P8ud4PK5gMKhYLKaMjAwv4wIYAfF4XJmZmSN+H/T0CKi3t1etra0KhUJf30BqqkKhkFpaWs7qNk6cOKFTp07poosuGvKc6upqZWZmJo9gMOhlTAAThKcAdXV1qa+vT4FAoN96IBBQJBI5q9tYvXq1ZsyY0S9i31RZWalYLJY8Ojs7vYwJYIKYNJYX27x5s3bt2qXm5malp6cPeZ7f75ff7x/DyQBY8BSgrKwspaWlKRqN9luPRqPKycn51r1btmzR5s2b9fbbb2vevHneJwVwzvH0FMzn86mgoEBNTU3JtUQioaamJhUVFQ2574knntDGjRvV2NioBQsWDH9aAOcUz0/BwuGwysvLtWDBAi1cuFA1NTXq7u7WypUrJUllZWWaOXOmqqurJUm///3vtX79er344ovKy8tLvlZ04YUX6sILLxzBXwXAROM5QKWlpTp69KjWr1+vSCSi/Px8NTY2Jl+Y7ujoUGrq1w+snnrqKfX29uoXv/hFv9upqqrSI4888v2mBzChef4ckIXR+gwCgLMzLj4HBAAjiQABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAmWEFqLa2Vnl5eUpPT1dhYaH27Nnzref/9a9/1WWXXab09HRdffXVamhoGNawAM4tngNUX1+vcDisqqoq7d27V/Pnz1dxcbGOHDky6PkffPCBbr31Vt1+++3at2+fli1bpmXLlumjjz763sMDmNhSnHPOy4bCwkJde+212rZtmyQpkUgo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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplot(1,2,1)\n",
    "sns.distplot(df['Season'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6e1c486-8c42-4d14-9b08-4df0a4b2532b",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.boxplot(df['State'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ee770b05-c216-4eed-9890-beec6db86b3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Area'>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df['Area'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "48242ec2-71c8-414b-9ebb-a2bdd804ee09",
   "metadata": {},
   "outputs": [],
   "source": [
    "Q1=df['Area'].quantile(0.25)\n",
    "Q3=df['Area'].quantile(0.45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7e89b6eb-4c5f-44c8-a6c4-41dffbb4335d",
   "metadata": {},
   "outputs": [],
   "source": [
    "IQR=Q3-Q1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0b78131d-047f-4dea-a70d-3b1ce589a46c",
   "metadata": {},
   "outputs": [],
   "source": [
    "min=Q1-1.5*IQR\n",
    "max=Q3+1.5*IQR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b725a438-a79c-40bf-a98b-9e739a0a47a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-6389.600000000005"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5bf80ed9-92ae-4e38-952c-e33dd0ce4a44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14356.000000000007"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1d7f57ef-abf7-4878-83cb-e9e7bc85387d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df[(df['Area']>min)&(df['Area']<max)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4e152823-0cf3-4a16-850c-3d6d0b162e0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Area'>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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AAAwENah6cSJE3r88ceVlJSkmJgY/fM//7N++ctfyrIsu8ayLBUUFKhnz56KiYlRWlqaPv7446Dj1NXVKTs7Wy6XS7GxscrJydHhw4eDarZv367rrrtO0dHRSkhIUGFh4TmZIwAAaB/COjQ999xzmjt3rl555RV9+OGHeu6551RYWKhZs2bZNYWFhZo5c6bmzZunsrIydenSRenp6Tp27Jhdk52drcrKShUXF2vFihUqKSlRbm6uPR4IBDRs2DD16tVL5eXlmj59uqZOnaqioqJzOl8AABC+IkPdwJls2LBBP/vZz5SRkSFJuuSSS7Ro0SJt2rRJ0pdXmV5++WU99thj+tnPfiZJ+t3vfiePx6Nly5YpKytLH374oVavXq3Nmzdr4MCBkqRZs2bpxhtv1PPPP6/4+HgtWLBAjY2N+s1vfqOoqChdeumlqqio0IsvvhgUrgAAwPkrrK80XXPNNVqzZo12794tSfrggw/0/vvv66c//akkac+ePfL5fEpLS7Pf43a7lZKSotLSUklSaWmpYmNj7cAkSWlpaYqIiFBZWZldM3jwYEVFRdk16enpqqqq0sGDB0/bW0NDgwKBQNAGAAA6rrC+0vTII48oEAioT58+6tSpk06cOKGnn35a2dnZkiSfzydJ8ng8Qe/zeDz2mM/nU1xcXNB4ZGSkunfvHlSTlJR0yjFaxrp163ZKb9OmTdMTTzzRBrMEAADtQVhfaVqyZIkWLFighQsXauvWrXr99df1/PPP6/XXXw91a5oyZYr8fr+97du3L9QtAQCAsyisrzRNmjRJjzzyiLKysiRJ/fv31969ezVt2jSNHj1aXq9XklRTU6OePXva76upqdEVV1whSfJ6vaqtrQ067vHjx1VXV2e/3+v1qqamJqim5XVLzVc5nU45nc7vPkkAANAuhPWVpi+++EIREcEtdurUSc3NzZKkpKQkeb1erVmzxh4PBAIqKytTamqqJCk1NVX19fUqLy+3a9auXavm5malpKTYNSUlJWpqarJriouLlZycfNqv5gAAwPknrEPTTTfdpKefflorV67U//3f/2np0qV68cUX9e///u+SJIfDofHjx+upp57S8uXLtWPHDt15552Kj49XZmamJKlv374aPny4xo4dq02bNmn9+vXKz89XVlaW4uPjJUl33HGHoqKilJOTo8rKSi1evFgzZszQxIkTQzV1AAAQZsL667lZs2bp8ccf13/913+ptrZW8fHxGjdunAoKCuyahx9+WEeOHFFubq7q6+s1aNAgrV69WtHR0XbNggULlJ+fr6FDhyoiIkIjRozQzJkz7XG326133nlHeXl5GjBggC666CIVFBSw3AAAALA5rJOX18a3FggE5Ha75ff75XK5Qt0OgDa0e/du5ebmqqioSL179w51OwDaUGvO39/qStMf//hHLVmyRNXV1WpsbAwa27p167c5JAAAQFhr9T1NM2fO1JgxY+TxeLRt2zb9+Mc/Vo8ePfTpp5/ai04CAAB0NK0OTXPmzFFRUZFmzZqlqKgoPfzwwyouLtb9998vv99/NnoEAAAIuVaHpurqal1zzTWSpJiYGB06dEiSNGrUKC1atKhtuwMAAAgTrQ5NXq9XdXV1kqTExERt3LhR0pfPgeOecgAA0FG1OjTdcMMNWr58uSRpzJgxmjBhgv71X/9Vt99+u71+EgAAQEfT6l/PFRUV2Sty5+XlqUePHtqwYYNuvvlmjRs3rs0bBAAACAetDk0RERFBjzbJysqynw0HAADQUX2rx6j85S9/0c9//nOlpqZq//79kqTf//73ev/999u0OQAAgHDR6tD03//930pPT1dMTIy2bdumhoYGSZLf79czzzzT5g0CAACEg1aHpqeeekrz5s3Tq6++qs6dO9v7r732WlYDBwAAHVarQ1NVVZUGDx58yn632636+vq26AkAACDsfKt1mj755JNT9r///vv6/ve/3yZNAQAAhJtWh6axY8fqgQceUFlZmRwOhw4cOKAFCxbooYce0r333ns2egQAAAi5Vi858Mgjj6i5uVlDhw7VF198ocGDB8vpdOqhhx7SfffddzZ6BAAACLlWhaYTJ05o/fr1ysvL06RJk/TJJ5/o8OHD6tevny688MKz1SMAAEDItSo0derUScOGDdOHH36o2NhY9evX72z1BQAAEFZafU/TZZddpk8//fRs9AIAABC2vtU6TQ899JBWrFihv/71rwoEAkEbAABAR9TqG8FvvPFGSdLNN98sh8Nh77csSw6HQydOnGi77gAAAMJEq0PTu++++7VjO3bs+E7NAAAAhKtWh6YhQ4YEvT506JAWLVqk1157TeXl5crPz2+z5gAAAMJFq+9palFSUqLRo0erZ8+eev7553XDDTdo48aNbdkbAABA2GjVlSafz6f58+fr17/+tQKBgG677TY1NDRo2bJlLD8AAAA6NOMrTTfddJOSk5O1fft2vfzyyzpw4IBmzZp1NnsDAAAIG8ZXmlatWqX7779f9957r374wx+ezZ4AAADCjvGVpvfff1+HDh3SgAEDlJKSoldeeUV/+9vfzmZvAAAAYcM4NF199dV69dVX9de//lXjxo3TG2+8ofj4eDU3N6u4uFiHDh06m30CAACEVKt/PdelSxfdddddev/997Vjxw49+OCDevbZZxUXF6ebb775bPQIAAAQct96yQFJSk5OVmFhoT777DMtWrSorXoCAAAIO98pNLXo1KmTMjMztXz58rY4HAAAQNhpk9AEAADQ0RGaAAAADBCaAAAADBCaAAAADBCaAAAADIR9aNq/f79+/vOfq0ePHoqJiVH//v21ZcsWe9yyLBUUFKhnz56KiYlRWlqaPv7446Bj1NXVKTs7Wy6XS7GxscrJydHhw4eDarZv367rrrtO0dHRSkhIUGFh4TmZHwAAaB/COjQdPHhQ1157rTp37qxVq1Zp165deuGFF9StWze7prCwUDNnztS8efNUVlamLl26KD09XceOHbNrsrOzVVlZqeLiYq1YsUIlJSXKzc21xwOBgIYNG6ZevXqpvLxc06dP19SpU1VUVHRO5wsAAMKYFcYmT55sDRo06GvHm5ubLa/Xa02fPt3eV19fbzmdTmvRokWWZVnWrl27LEnW5s2b7ZpVq1ZZDofD2r9/v2VZljVnzhyrW7duVkNDQ9BnJycnG/fq9/stSZbf7zd+D4D2oaqqyhoyZIhVVVUV6lYAtLHWnL/D+krT8uXLNXDgQP3Hf/yH4uLidOWVV+rVV1+1x/fs2SOfz6e0tDR7n9vtVkpKikpLSyVJpaWlio2N1cCBA+2atLQ0RUREqKyszK4ZPHiwoqKi7Jr09HRVVVXp4MGDp+2toaFBgUAgaAMAAB1XWIemTz/9VHPnztUPf/hDvf3227r33nt1//336/XXX5ck+Xw+SZLH4wl6n8fjscd8Pp/i4uKCxiMjI9W9e/egmtMd4+TP+Kpp06bJ7XbbW0JCwnecLQAACGdhHZqam5t11VVX6ZlnntGVV16p3NxcjR07VvPmzQt1a5oyZYr8fr+97du3L9QtAQCAsyisQ1PPnj3Vr1+/oH19+/ZVdXW1JMnr9UqSampqgmpqamrsMa/Xq9ra2qDx48ePq66uLqjmdMc4+TO+yul0yuVyBW0AAKDjCuvQdO2116qqqipo3+7du9WrVy9JUlJSkrxer9asWWOPBwIBlZWVKTU1VZKUmpqq+vp6lZeX2zVr165Vc3OzUlJS7JqSkhI1NTXZNcXFxUpOTg76pR4AADh/hXVomjBhgjZu3KhnnnlGn3zyiRYuXKiioiLl5eVJkhwOh8aPH6+nnnpKy5cv144dO3TnnXcqPj5emZmZkr68MjV8+HCNHTtWmzZt0vr165Wfn6+srCzFx8dLku644w5FRUUpJydHlZWVWrx4sWbMmKGJEyeGauoAACDMRIa6gTP50Y9+pKVLl2rKlCl68sknlZSUpJdfflnZ2dl2zcMPP6wjR44oNzdX9fX1GjRokFavXq3o6Gi7ZsGCBcrPz9fQoUMVERGhESNGaObMmfa42+3WO++8o7y8PA0YMEAXXXSRCgoKgtZyAgAA5zeHZVlWqJvoCAKBgNxut/x+P/c3AR3M7t27lZubq6KiIvXu3TvU7QBoQ605f4f113MAAADhgtAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABgIKyfPYfQqKmpkd/vD3UbQNjYu3dv0D8B/H9ut1sejyfUbZwTPHuujXSUZ8/V1NTo56PuVFNjQ6hbAQC0A52jnPrD73/XboNTa87fXGlCEL/fr6bGBh39/hA1R7tD3Q4AIIxFHPNLn66T3+9vt6GpNQhNOK3maLeau1wU6jYAAAgb3AgOAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABgoF2FpmeffVYOh0Pjx4+39x07dkx5eXnq0aOHLrzwQo0YMUI1NTVB76uurlZGRoYuuOACxcXFadKkSTp+/HhQzXvvvaerrrpKTqdTP/jBDzR//vxzMCMAANBetJvQtHnzZv3qV7/Sv/zLvwTtnzBhgv785z/rzTff1Lp163TgwAHdcsst9viJEyeUkZGhxsZGbdiwQa+//rrmz5+vgoICu2bPnj3KyMjQT37yE1VUVGj8+PG6++679fbbb5+z+QEAgPDWLkLT4cOHlZ2drVdffVXdunWz9/v9fv3617/Wiy++qBtuuEEDBgzQb3/7W23YsEEbN26UJL3zzjvatWuX/vCHP+iKK67QT3/6U/3yl7/U7Nmz1djYKEmaN2+ekpKS9MILL6hv377Kz8/Xrbfeqpdeeikk8wUAAOGnXYSmvLw8ZWRkKC0tLWh/eXm5mpqagvb36dNHiYmJKi0tlSSVlpaqf//+8ng8dk16eroCgYAqKyvtmq8eOz093T7G6TQ0NCgQCARtAACg44oMdQPf5I033tDWrVu1efPmU8Z8Pp+ioqIUGxsbtN/j8cjn89k1JwemlvGWsTPVBAIBHT16VDExMad89rRp0/TEE09863kBAID2JayvNO3bt08PPPCAFixYoOjo6FC3E2TKlCny+/32tm/fvlC3BAAAzqKwDk3l5eWqra3VVVddpcjISEVGRmrdunWaOXOmIiMj5fF41NjYqPr6+qD31dTUyOv1SpK8Xu8pv6Zref1NNS6X67RXmSTJ6XTK5XIFbQAAoOMK69A0dOhQ7dixQxUVFfY2cOBAZWdn2//euXNnrVmzxn5PVVWVqqurlZqaKklKTU3Vjh07VFtba9cUFxfL5XKpX79+ds3Jx2ipaTkGAABAWN/T1LVrV1122WVB+7p06aIePXrY+3NycjRx4kR1795dLpdL9913n1JTU3X11VdLkoYNG6Z+/fpp1KhRKiwslM/n02OPPaa8vDw5nU5J0j333KNXXnlFDz/8sO666y6tXbtWS5Ys0cqVK8/thAEAQNgK69Bk4qWXXlJERIRGjBihhoYGpaena86cOfZ4p06dtGLFCt17771KTU1Vly5dNHr0aD355JN2TVJSklauXKkJEyZoxowZuvjii/Xaa68pPT09FFMCAABhqN2Fpvfeey/odXR0tGbPnq3Zs2d/7Xt69eqlt95664zHvf7667Vt27a2aBEAAHRAYX1PEwAAQLggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABggNAEAABgI69A0bdo0/ehHP1LXrl0VFxenzMxMVVVVBdUcO3ZMeXl56tGjhy688EKNGDFCNTU1QTXV1dXKyMjQBRdcoLi4OE2aNEnHjx8Pqnnvvfd01VVXyel06gc/+IHmz59/tqcHAADakbAOTevWrVNeXp42btyo4uJiNTU1adiwYTpy5IhdM2HCBP35z3/Wm2++qXXr1unAgQO65ZZb7PETJ04oIyNDjY2N2rBhg15//XXNnz9fBQUFds2ePXuUkZGhn/zkJ6qoqND48eN199136+233z6n8wUAAOHLYVmWFeomTH3++eeKi4vTunXrNHjwYPn9fv3TP/2TFi5cqFtvvVWS9NFHH6lv374qLS3V1VdfrVWrVunf/u3fdODAAXk8HknSvHnzNHnyZH3++eeKiorS5MmTtXLlSu3cudP+rKysLNXX12v16tVGvQUCAbndbvn9frlcrraf/Dmye/du5ebm6ki/m9Xc5aJQtwMACGMRR/6mLruWq6ioSL179w51O99Ka87fYX2l6av8fr8kqXv37pKk8vJyNTU1KS0tza7p06ePEhMTVVpaKkkqLS1V//797cAkSenp6QoEAqqsrLRrTj5GS03LMQAAACJD3YCp5uZmjR8/Xtdee60uu+wySZLP51NUVJRiY2ODaj0ej3w+n11zcmBqGW8ZO1NNIBDQ0aNHFRMTc0o/DQ0NamhosF8HAoHvNkEAABDW2s2Vpry8PO3cuVNvvPFGqFuR9OVN6m63294SEhJC3RIAADiL2kVoys/P14oVK/Tuu+/q4osvtvd7vV41Njaqvr4+qL6mpkZer9eu+eqv6Vpef1ONy+U67VUmSZoyZYr8fr+97du37zvNEQAAhLewDk2WZSk/P19Lly7V2rVrlZSUFDQ+YMAAde7cWWvWrLH3VVVVqbq6WqmpqZKk1NRU7dixQ7W1tXZNcXGxXC6X+vXrZ9ecfIyWmpZjnI7T6ZTL5QraAABAxxXW9zTl5eVp4cKF+p//+R917drVvgfJ7XYrJiZGbrdbOTk5mjhxorp37y6Xy6X77rtPqampuvrqqyVJw4YNU79+/TRq1CgVFhbK5/PpscceU15enpxOpyTpnnvu0SuvvKKHH35Yd911l9auXaslS5Zo5cqVIZt7qEUcrQ91CwCAMHe+nSvCOjTNnTtXknT99dcH7f/tb3+r//zP/5QkvfTSS4qIiNCIESPU0NCg9PR0zZkzx67t1KmTVqxYoXvvvVepqanq0qWLRo8erSeffNKuSUpK0sqVKzVhwgTNmDFDF198sV577TWlp6ef9TmGq5g9JaFuAQCAsNKu1mkKZx1tnaajSYPVHBMb6nYAAGEs4mi9YvaUnDfrNIX1lSaETnNMLItbAgBwkrC+ERwAACBcEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMEJoAAAAMRIa6AYSniGP+ULcAAAhz59u5gtCEIG63W52jnNKn60LdCgCgHegc5ZTb7Q51G+cEoQlBPB6P/vD738nvP7/+9gCcyd69e/X000/r0UcfVa9evULdDhBW3G63PB5PqNs4JwhNOIXH4zlv/gcAWqNXr17q3bt3qNsAECLcCA4AAGCA0AQAAGCA0PQVs2fP1iWXXKLo6GilpKRo06ZNoW4JAACEAULTSRYvXqyJEyfqF7/4hbZu3arLL79c6enpqq2tDXVrAAAgxAhNJ3nxxRc1duxYjRkzRv369dO8efN0wQUX6De/+U2oWwMAACHGr+f+obGxUeXl5ZoyZYq9LyIiQmlpaSotLT2lvqGhQQ0NDfbrQCBwTvrE+ePYsWOqrq4OdRvQl0sOnPxPhF5iYqKio6ND3QbOM4Smf/jb3/6mEydOnPJTe4/Ho48++uiU+mnTpumJJ544V+3hPFRdXa3c3NxQt4GTPP3006FuAf9QVFTE8g845whN39KUKVM0ceJE+3UgEFBCQkIIO0JHk5iYqKKiolC3AYSlxMTEULeA8xCh6R8uuugiderUSTU1NUH7a2pq5PV6T6l3Op1yOp3nqj2ch6Kjo/mbNACEEW4E/4eoqCgNGDBAa9assfc1NzdrzZo1Sk1NDWFnAAAgHHCl6SQTJ07U6NGjNXDgQP34xz/Wyy+/rCNHjmjMmDGhbg0AAIQYoekkt99+uz7//HMVFBTI5/Ppiiuu0OrVq3kOGwAAkMOyLCvUTXQEgUBAbrdbfr9fLpcr1O0AAAADrTl/c08TAACAAUITAACAAUITAACAAUITAACAAUITAACAAUITAACAAUITAACAAUITAACAAUITAACAAR6j0kZaFlYPBAIh7gQAAJhqOW+bPCCF0NRGDh06JElKSEgIcScAAKC1Dh06JLfbfcYanj3XRpqbm3XgwAF17dpVDocj1O0AaEOBQEAJCQnat28fz5YEOhjLsnTo0CHFx8crIuLMdy0RmgDgG/BAbgASN4IDAAAYITQBAAAYIDQBwDdwOp36xS9+IafTGepWAIQQ9zQBAAAY4EoTAACAAUITAACAAUITAACAAUITAACAAUITAACAAUITAACAAUITAACAAUITAACAgf8H97pQPLwwmzwAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df['Area'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "96767146-7ff9-4165-8495-f1a603dd1e26",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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WhU7j0GDBlm0Qa1atVJOTo6OHDlyzW3zf3bekxpt2rTRH3/8obS0tGJ9PoAbR9tU+t89xo4daz7HeZOfn58SExO1f/9+9ezZU3///bdOnTqlU6dOKSMjQ+3bt9eWLVsKjCJ7ZXtU2vbu3at+/frpscce05gxYyRdfnLuf//7n7p06SLDMMx5nzp1SmFhYUpLSyvQjkRERFhc91E6eH0PVnH//fdbFEeefvppNW3aVFFRUercubNMJpOOHDmigIAAVa1a1WLbvEdS8/8yaDKZNH/+fN13331yc3PTggULCi1iODo6WlzcJal27dqSVGQ/FydPntT58+dVp06dAuvq1aun3Nxc/fnnn2rQoEHxDv7/y8u/qP2uXbv2hjoeHzt2rFq1aiUnJydVr15d9erVK3RUiuDg4AJ5OTo66s4777RY7ufnJy8vL3PeeX/eddddFnE1atQo8OpEceW9Ynj33Xdf1/ZXup5zXLNmTYu4vGM5c+aMPDw8rJIXUJ5xfS/d6/snn3yi+++/X3///bf+/vtvSVLTpk2VlZWl5cuXa9CgQRbxV17TpMvXtcIKWNa8/l24cMHcEfvRo0ct+k+xVjEmr507d+6cPvvsM3PB7kqrVq3S66+/rsTERIu+EYt7s+Nq5+VavvvuO40bN04JCQkF+idMS0uTp6dnsXIAJGnLli2aMmWKduzYoePHj+uzzz5T165dS7QPwzA0depUzZs3T0eOHFH16tX13HPPafTo0aWTdBlB21T63z0aNmxY6KAb+/fvl3S5YFOUtLQ0i+8PV34/KU3p6el6/PHHdeutt+qjjz4y/z2ePHlSqampmjdvnubNm1fotnkdwuexZd4VGUUplApHR0e1a9dOM2fO1P79+0t8kZWktWvXSro80sH+/fsr/EWhqIbhSkVV86/nyaSiFLWvvI4gy5L8/QDkl/8LFYDi4/puPfv379f27dslFbwhIF3ua+rKolRJrmnXii3JtXzo0KFasGCBhg0bppCQEHl6esrBwUE9evQocEf8euVv57p27arz589r4MCBevDBBxUYGChJ+uabb/Too4+qdevWmj17tvz9/eXi4qIFCxaYB9C4luttFw4ePKj27durbt26mjZtmgIDA2UymbR69WpNnz7daucBFUdGRoYaN26sfv366fHHH7+ufbzwwgtat26d3n77bTVs2FCnT5/W6dOnrZxp2UfbZDt517opU6aoSZMmhcZc2T+sLZ826tOnj44dO6YffvjB4gZMXt7PPPNMkQW1Ro0aWczzlJRtUJRCqbl06ZIkmTucCwoK0vr163X27FmLOxa//fabeX2eX375RRMnTlTfvn2VmJioAQMGaNeuXQXuQObm5uqPP/4w36GQpN9//12SCnR4nadGjRqqVKmS9u3bV2Ddb7/9JkdHR/MvvyUp5OTlX9R+q1evft13Km5EUFCQcnNztX//fouOElNSUpSammrOO+/P/fv3W9wBOnnyZIG7x3l3PlJTUy2Glr3y1Ye8V0x2795d4Emt/Ip7nsvqOQYqGq7vlvu93mvPokWL5OLioo8//rhAoeTbb7/VO++8o6SkpEKfjrKG/Nfy/Ap7je2///2vIiIiNHXqVPOyixcvFtjWmt5880199tlneuONNzR37lxJ0v/+9z+5ublp7dq1cnV1NccuWLCg1PLI8+WXXyozM1NffPGFxd/Jpk2bSv2zUT517NhRHTt2LHJ9ZmamRo8erU8//VSpqam6++679dZbb5lHHPv11181Z84c7d692/y0TEUupNA2We63tH4vzvv93sPDo1g3zItizRvmed58802tXLlSK1asUN26dS3W1ahRQ1WrVlVOTs4N5Q3ro08plIrs7GytW7dOJpPJXAjp1KmTcnJy9N5771nETp8+XQ4ODuZGOTs7W3369FFAQIBmzpyp2NhYpaSkaPjw4YV+Vv79GYah9957Ty4uLmrfvn2h8U5OTurQoYM+//xzi8dsU1JStHjxYj344IPmqnrehbw4v3T7+/urSZMmWrhwoUX87t27tW7dOnXq1Oma+ygNeZ87Y8YMi+V5o4vkjVQUGhoqFxcXvfvuuxZ3i6/cTvqnMdqyZYt5WV4fV/l16NBBVatWVUxMTIHhzfN/RuXKlYv1+kdZPcdARcL1/Z/4G732LFq0SK1atdJTTz2lJ554wmJ66aWXJEmffvrpde27ODw8PFS9enWLa7kkzZ49u0Csk5NTgSeJ3n333VJ9QvaOO+5Qt27dFBsbq+TkZHMeDg4OFp97+PBhrVy5stTyyJNXOLzy1UVbFMRQMUVFRSkhIUFLlizRL7/8ou7du+uRRx4xvz715Zdf6vbbb9eqVasUHBysWrVqacCAARXySSnapn/iS/v34mbNmumOO+7Q22+/XWC0O+nyDe3iKMmxFsf69es1ZswYjR49utDXYJ2cnNStWzf973//0+7duwusL27esD6elIJVfPXVV+a7DidOnNDixYu1f/9+vfLKK+aLbJcuXdSuXTuNHj1ahw8fVuPGjbVu3Tp9/vnnGjZsmLnQkddPxIYNG1S1alU1atRIY8eO1ZgxY/TEE09YXGDd3Ny0Zs0aRUREqHnz5vrqq68UFxenV199VTVq1Cgy39dff13x8fF68MEH9dxzz8nZ2Vn/+c9/lJmZqcmTJ5vjmjRpIicnJ7311ltKS0uTq6urHnroIfn4+BS63ylTpqhjx44KCQlR//79zcOyenp6avz48Td6mq9L48aNFRERoXnz5ik1NVVt2rTRDz/8oIULF6pr165q166dpMt3D1588UXFxMSoc+fO6tSpk3bu3KmvvvpK1atXt9hnhw4dVLNmTfXv318vvfSSnJycNH/+fNWoUUNJSUnmOA8PD02fPl0DBgzQfffdp549e6patWr6+eefdf78eXMRq1mzZlq6dKmio6N13333qUqVKurSpUuhx1MWzzFQnnF9v8za155t27bpwIEDFh3m5nfrrbfqnnvu0aJFi/Tyyy+XeP/FNWDAAL355psaMGCA7r33Xm3ZssV81z+/zp076+OPP5anp6fq16+vhIQErV+/3jzMdml56aWXtGzZMs2YMUNvvvmmwsPDNW3aND3yyCPq2bOnTpw4oVmzZunOO+/UL7/8Uqq5dOjQQSaTSV26dNH//d//6dy5c3r//ffl4+Oj48ePl+pno+JJSkrSggULlJSUpICAAEnSiy++qDVr1mjBggWaNGmS/vjjDx05ckTLly/XRx99pJycHA0fPlxPPPGENm7caOcjKF20TZfZ4/diR0dHffDBB+rYsaMaNGigvn376tZbb9XRo0e1adMmeXh46Msvv7zmfpo1ayZJev755xUWFiYnJyf16NHjuvN6+umnVaNGDd1111365JNPLNY9/PDD8vX11ZtvvqlNmzapefPmGjhwoOrXr6/Tp0/rp59+0vr16ytkQbdMsPVwfyhfChuW1c3NzWjSpIkxZ84ci2FCDcMwzp49awwfPtwICAgwXFxcjLvuusuYMmWKOW7Hjh2Gs7OzxVCrhmEYly5dMu677z4jICDAOHPmjGEY/wzXfPDgQaNDhw5GpUqVDF9fX2PcuHFGTk6Oxfa6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dt3JAABuXvZqKx555BE9/vjjCg4O1sGDB/Xqq6+qY8eOSkhIkJOTk5KTk+Xj42OxjbOzs7y9vZWcnCxJSk5OVnBwsEWMr6+veV21atUKfG5MTIwmTJhgteMAABSO7yIAUH4Vqyi1c+fOYu3MwcHhhpIBANy87NVW9OjRw/xzw4YN1ahRI91xxx3avHmz2rdvb9XPym/UqFEWX5TS09MVGBhYap8HABVVabcvs2bN0pQpU5ScnKzGjRvr3Xff1f33319kfGpqqkaPHq0VK1bo9OnTCgoK0owZM9SpU6fr+nwAqMiKVZTatGlTaecBALjJlZW24vbbb1f16tV14MABtW/fXn5+fjpx4oRFzKVLl3T69GlzP1R+fn5KSUmxiMmbL6qvKldX1wIdqgMArK8025elS5cqOjpac+fOVfPmzTVjxgzz69tXPmUrSVlZWXr44Yfl4+Oj//73v7r11lt15MgReXl5lVqOAFCe0acUAKBc+euvv/T333/L399fkhQSEqLU1FTt2LHDHLNx40bl5uaqefPm5pgtW7YoOzvbHBMfH686deoU+uoeAKB8mDZtmgYOHKi+ffuqfv36mjt3ripVqqT58+cXGj9//nydPn1aK1euVMuWLVWrVi21adNGjRs3tnHmAFA+lHj0PUn68ccftWzZMiUlJSkrK8ti3YoVK6ySGADg5mattuLcuXM6cOCAef7QoUNKTEyUt7e3vL29NWHCBHXr1k1+fn46ePCgRo4cqTvvvFNhYWGSpHr16umRRx7RwIEDNXfuXGVnZysqKko9evRQQECAJKlnz56aMGGC+vfvr5dfflm7d+/WzJkzNX36dCucCQCANVmrfcnKytKOHTs0atQo8zJHR0eFhoYqISGh0G2++OILhYSEKDIyUp9//rlq1Kihnj176uWXX5aTk9P1HRAAVGAlflJqyZIleuCBB/Trr7/qs88+U3Z2tvbs2aONGzfK09OzNHIEANxkrNlW/Pjjj2ratKmaNm0q6XKHt02bNtXYsWPl5OSkX375RY8++qhq166t/v37q1mzZvrmm28sXq1btGiR6tatq/bt26tTp0568MEHNW/ePPN6T09PrVu3TocOHVKzZs00YsQIjR07VoMGDbLOCQEAWIU125dTp04pJyfHPLBFHl9fX/NAGFf6448/9N///lc5OTlavXq1/v3vf2vq1Kl6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o7fffluGYUiSLly4oLp166pu3bq6cOGCebvTp0/L399fDzzwgHJyciRJffr0UZUqVfTHH38oLCxMlStXVkBAgCZOnGje39Xs3LlTHTt2lIeHh6pUqaL27dvr+++/N6+PjY1V9+7dJUnt2rUzvy5yrf6UNm7cqFatWqly5cry8vLSY489pl9//dW8vk+fPmrTpo0kqXv37nJwcLiuvjkeeughSdKhQ4fMy7766ivzZ1etWlXh4eHas2ePxXbJycnq27evbrvtNrm6usrf31+PPfaY+ZWRWrVqac+ePfr666/Nx5yXX1F9Sm3btk2dOnVStWrVVLlyZTVq1EgzZ840ry+sT6nMzEwNHz5cNWrUUNWqVfXoo4/qr7/+KvRYjx49qn79+snX11eurq5q0KCB5s+fX+JzBqD8ob2xXnuTV3h65ZVXzMWsoUOHysXFxeKaXlifUpmZmRo3bpzuvPNOubq6KjAwUCNHjlRmZuY1z8+ePXv00EMPyd3dXbfddptef/115ebmXnM7AABQ9vFoAmwiLS1Np06dkmEYOnHihN59912dO3dOzzzzjDnGMAw9+uij2rRpk/r3768mTZpo7dq1eumll3T06FFNnz5d7u7uWrhwoVq2bKnRo0dr2rRpkqTIyEilpaUpNjZWTk5O5n3m5OTokUceUYsWLTR58mStWbNG48aN06VLlzRx4sQi892zZ49atWolDw8PjRw5Ui4uLvrPf/6jtm3b6uuvv1bz5s3VunVrPf/883rnnXf06quvql69epJk/rMw69evV8eOHXX77bdr/PjxunDhgt599121bNlSP/30k2rVqqX/+7//06233qpJkyaZX8nz9fUt8Tk/ePCgJOmWW26RJH388ceKiIhQWFiY3nrrLZ0/f15z5szRgw8+qJ07d5pfB+nWrZv27NmjoUOHqlatWjpx4oTi4+OVlJSkWrVqacaMGRo6dKiqVKmi0aNHS9JV84uPj1fnzp3l7++vF154QX5+fvr111+1atUqvfDCC0VuN2DAAH3yySfq2bOnHnjgAW3cuFHh4eEF4lJSUtSiRQs5ODgoKipKNWrU0FdffaX+/fsrPT1dw4YNK/G5A3Dzor25rLTam9mzZ6tBgwYaPny4nnzySX3xxReaO3eu/Pz8itwmNzdXjz76qL799lsNGjRI9erV065duzR9+nT9/vvvWrly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vXK7aW/VATDwDBq0ZT+6bWkdAEA5lfUnllmzZuUHP/hBrrnmmowYMSKtra1pbW3N+vXrkySPPfZYLrjggqxatSr/9V//leuvvz4zZszIQQcdlL322itJMnXq1EycODHHH398/vM//zM33XRTzjrrrMyaNSs1NTVJklNOOSV/+MMfcsYZZ+Thhx/OFVdckcWLF+f0008v27nD39u0aVOv1gEw8AwePLhX6wAAyqmsodSVV16Z9vb2TJ48OaNHjy4u1157bZKkuro6t9xyS6ZOnZpdd901X/jCF3LkkUfm5z//efEYgwcPzg033JDBgwenqakpn/70pzNjxoycf/75xZoJEybkxhtvzNKlS7P33nvn4osvzre//e00NzeX/Jzhtbz88su9WgfAwCOUAgAGkrJOdF4oFF53/9ixY3PHHXe84XHGjx+fX/ziF69bM3ny5Nx///096g9KadCgQenq6tqiOgAq04YNG3q1DgCgnPx2C/3EK7eb9lYdAAAA9GdCKegnRowY0at1AAAA0J8JpaCfGDp0aK/WAQAAQH8mlAIAAACg5IRS0E+88MILvVoHAAAA/ZlQCvoJT1QCAACgkgiloJ8oFAq9WgcAAAD9mVAK+ona2tperQMAAID+TCgF/URVVVWv1gEAAEB/JpSCfuKll17q1ToAAADoz4RS0E+8/PLLvVoHAAAA/ZlQCvoJV0oB8EYGDdqyH922tA4AoJz8xAL9RFdXV6/WATDwDB48uFfrAADKSSgFwIAzb968vO9978uIESMyatSoHHHEEXnkkUfe8HU//OEPs+uuu6a2tjZ77rlnfvGLX5SgW9hyrpQCAAYSP7EAMODccccdmTVrVu6+++4sXbo0mzZtytSpU7Nu3brXfM2KFStyzDHHZObMmbn//vtzxBFH5IgjjsiDDz5Yws7h9W3cuLFX6wAAymlIuRsAgN62ZMmSbusLFy7MqFGjsmrVqhx00EGbfc1ll12Www47LF/84heTJBdccEGWLl2ab37zm5k/f36f9wxbolAo9GodAEA5uVIKgAGvvb09STJy5MjXrFm5cmWmTJnSbVtzc3NWrly52frOzs50dHR0WwAAgC0nlAJgQOvq6sppp52WSZMmZY899njNutbW1jQ0NHTb1tDQkNbW1s3Wz5s3L/X19cVl7Nixvdo3AAAMdEIpAAa0WbNm5cEHH8yiRYt69bhz585Ne3t7cXniiSd69fgAADDQmVMKgAFr9uzZueGGG7J8+fLsuOOOr1vb2NiYtra2btva2trS2Ni42fqamprU1NT0Wq8AAFBpXCkFwIBTKBQye/bs/PSnP82tt96aCRMmvOFrmpqasmzZsm7bli5dmqampr5qEwAAKporpQAYcGbNmpVrrrkmP/vZzzJixIjivFD19fUZNmxYkmTGjBl5xzvekXnz5iVJTj311Bx88MG5+OKLM3369CxatCj33ntvFixYULbzAACAgcyVUgAMOFdeeWXa29szefLkjB49urhce+21xZqWlpY8/fTTxfUDDzww11xzTRYsWJC99947P/rRj3Lddde97uToAADAm+dKKQAGnEKh8IY1t99++6u2ffKTn8wnP/nJPugIesfIkSPz3HPPbVEdAEB/50opAICtRGdnZ6/WAQCUk1AK+onBgwf3ah0AA8+6det6tQ4AoJyEUtBP1NXV9WodAAAA9GdCKegnhg8f3qt1AAAA0J8JpaCfePbZZ3u1DgAAAPozoRT0Exs2bOjVOgAAAOjPhFIAAAAAlJxQCgAAAICSE0pBPzFo0JZ9O25pHQAAAPRnfruFfqKrq6tX6wAAAKA/E0oBAAAAUHJCKQAAAABKTigFAAAAQMkJpQAAthIeigEADCR+YgEA2Ep4KAYAMJAIpQAAAAAoOaEUAAAAACUnlAIAAACg5IRSAAAAAJScUAoAAACAkhtS7gYAAN6KDRs2pKWlpdxt9Du/+93vyt1CSYwbNy61tbXlbgMAeBOEUgDAVq2lpSUnn3xyudvodyrla7JgwYLsvPPO5W4DAHgThFIAwFZt3LhxWbBgQbnbKImFCxdmxYoVb1h34IEH5jOf+UzfN9QPjBs3rtwtAABvklAK+omqqqoUCoUtqgPgv9XW1lbMlTL/7//9v0ybNm2L6oYNG1aCjgAA3jwTnUM/sSWBVE/qABh4hg0blkmTJr1uzaRJkwRSAMBWQSgFALAVufDCC18zmJo0aVIuvPDCEncEAPDmuH0PAGArc+GFF2b9+vX5yle+kttvvz2TJ0/Ol770JVdIAQBblbJeKTVv3ry8733vy4gRIzJq1KgcccQReeSRR7rVbNiwIbNmzcrb3va2bLvttjnyyCPT1tbWraalpSXTp0/PNttsk1GjRuWLX/xiXnrppW41t99+e/bdd9/U1NRkp512ysKFC/v69AAA+sywYcNy7LHHJkmOPfZYgRQAsNUpayh1xx13ZNasWbn77ruzdOnSbNq0KVOnTs26deuKNaeffnp+/vOf54c//GHuuOOOPPXUU/nEJz5R3P/yyy9n+vTp2bhxY1asWJF/+7d/y8KFC3P22WcXa9asWZPp06fnkEMOyerVq3Paaafls5/9bG666aaSni8AAAAAf1XW2/eWLFnSbX3hwoUZNWpUVq1alYMOOijt7e35zne+k2uuuSYf/vCHkyTf/e53s9tuu+Xuu+/OBz7wgdx88835zW9+k1tuuSUNDQ3ZZ599csEFF+RLX/pSzj333FRXV2f+/PmZMGFCLr744iTJbrvtljvvvDOXXnppmpubS37eAAAAAJWuX0103t7eniQZOXJkkmTVqlXZtGlTpkyZUqzZddddM27cuKxcuTJJsnLlyuy5555paGgo1jQ3N6ejoyMPPfRQseZvj/FKzSvHAAAAAKC0+s1E511dXTnttNMyadKk7LHHHkmS1tbWVFdXZ7vttutW29DQkNbW1mLN3wZSr+x/Zd/r1XR0dGT9+vWvmoOhs7MznZ2dxfWOjo63foIAAAAAFPWbK6VmzZqVBx98MIsWLSp3K5k3b17q6+uLy9ixY8vdEgAAAMCA0i9CqdmzZ+eGG27Ibbfdlh133LG4vbGxMRs3bswLL7zQrb6trS2NjY3Fmr9/Gt8r629UU1dXt9kn1cydOzft7e3F5YknnnjL5wgAAADAfytrKFUoFDJ79uz89Kc/za233poJEyZ027/ffvtl6NChWbZsWXHbI488kpaWljQ1NSVJmpqa8utf/zrPPPNMsWbp0qWpq6vLxIkTizV/e4xXal45xt+rqalJXV1dtwUAAACA3lPWOaVmzZqVa665Jj/72c8yYsSI4hxQ9fX1GTZsWOrr6zNz5szMmTMnI0eOTF1dXT7/+c+nqakpH/jAB5IkU6dOzcSJE3P88cfnoosuSmtra84666zMmjUrNTU1SZJTTjkl3/zmN3PGGWfkH/7hH3Lrrbdm8eLFufHGG8t27gAAAACVrKyh1JVXXpkkmTx5crft3/3ud/OZz3wmSXLppZdm0KBBOfLII9PZ2Znm5uZcccUVxdrBgwfnhhtuyOc+97k0NTVl+PDhOeGEE3L++ecXayZMmJAbb7wxp59+ei677LLsuOOO+fa3v53m5uY+P0femg0bNqSlpaXcbfQ7v/vd78rdQkmMGzcutbW15W4DAACAPlBVKBQK5W6iv+vo6Eh9fX3a29vdyldiv/vd73LyySeXuw3KZMGCBdl5553L3UZF8Xn35vnaUQ6vjJM+Lykln3cA9JayXikFb2TcuHFZsGBBudsoiZ///Of5+c9//oZ1hx9+eA4//PASdFR+48aNK3cLAAAA9BGhFP1abW1txfzl9/Of//wWhVKf//znU11dXYKOAAAAoO+U9el7wH+rrq7O0Ucf/bo1Rx99tEAKAACAAcGVUtCPnHLKKUmSxYsXp6urq7h90KBBOeqoo4r7AQAAYGvnSinoZ0455ZQsWbIkRx11VJLkqKOOypIlSwRSAAAADChCKeiHqqurM2XKlCTJlClT3LIHAADAgCOUAgAAAKDkhFIAAAAAlJxQCgAAAICSE0oBAAAAUHJCKQAAAABKTigFAAAAQMkJpQAAAAAoOaEUAAAAACUnlAIAAACg5IRSAAAAAJScUAoAAACAkhNKAQAAAFByQikAAAAASk4oBQAAAEDJCaUAAAAAKDmhFAAAAAAlJ5QCAAAAoOSEUgAMOMuXL8/hhx+eMWPGpKqqKtddd93r1t9+++2pqqp61dLa2lqahgEAoAIJpQAYcNatW5e99947l19+eY9e98gjj+Tpp58uLqNGjeqjDgEAgCHlbgAAetu0adMybdq0Hr9u1KhR2W677Xq/IQAA4FVcKQUA/7999tkno0ePzkc+8pHcddddr1vb2dmZjo6ObgsAALDlhFIAVLzRo0dn/vz5+fGPf5wf//jHGTt2bCZPnpz77rvvNV8zb9681NfXF5exY8eWsGMAANj6uX0PgIq3yy67ZJdddimuH3jggXnsscdy6aWX5vvf//5mXzN37tzMmTOnuN7R0SGYAgCAHhBKAcBmvP/978+dd975mvtrampSU1NTwo4AAGBgcfseAGzG6tWrM3r06HK3AQAAA5YrpQAYcNauXZtHH320uL5mzZqsXr06I0eOzLhx4zJ37tz88Y9/zPe+970kyde+9rVMmDAhu+++ezZs2JBvf/vbufXWW3PzzTeX6xQAAGDAE0oBMODce++9OeSQQ4rrr8z9dMIJJ2ThwoV5+umn09LSUty/cePGfOELX8gf//jHbLPNNtlrr71yyy23dDsGAADQu4RSAAw4kydPTqFQeM39Cxcu7LZ+xhln5IwzzujjrgAAgL9lTikAAAAASk4oBQAAAEDJCaUAAAAAKDmhFAAAAAAlJ5QCAAAAoOSEUgAAAACUnFAKAAAAgJITSgEAAABQckIpAAAAAEpOKAUAAABAyQmlAAAAACg5oRQAAAAAJSeUAgAAAKDkhFIAAAAAlJxQCgAAAICSE0oBAAAAUHJCKQAAAABKrqyh1PLly3P44YdnzJgxqaqqynXXXddt/2c+85lUVVV1Ww477LBuNc8991yOO+641NXVZbvttsvMmTOzdu3abjUPPPBAPvShD6W2tjZjx47NRRdd1NenBgAAAMDrKGsotW7duuy99965/PLLX7PmsMMOy9NPP11c/v3f/73b/uOOOy4PPfRQli5dmhtuuCHLly/PySefXNzf0dGRqVOnZvz48Vm1alW++tWv5txzz82CBQv67LwAAAAAeH1Dyvnm06ZNy7Rp0163pqamJo2NjZvd99vf/jZLlizJf/zHf2T//fdPknzjG9/IRz/60fzLv/xLxowZk6uvvjobN27MVVddlerq6uy+++5ZvXp1Lrnkkm7hFQAAAACl0+/nlLr99tszatSo7LLLLvnc5z6XP//5z8V9K1euzHbbbVcMpJJkypQpGTRoUH71q18Vaw466KBUV1cXa5qbm/PII4/k+eefL92JAAAAAFBU1iul3shhhx2WT3ziE5kwYUIee+yxfPnLX860adOycuXKDB48OK2trRk1alS31wwZMiQjR45Ma2trkqS1tTUTJkzoVtPQ0FDct/3227/qfTs7O9PZ2Vlc7+jo6O1TAwAAAKho/TqUOvroo4v/3nPPPbPXXnvl3e9+d26//fYceuihffa+8+bNy3nnnddnxwcAAACodP3+9r2/9a53vSs77LBDHn300SRJY2NjnnnmmW41L730Up577rniPFSNjY1pa2vrVvPK+mvNVTV37ty0t7cXlyeeeKK3TwUAAACgom1VodSTTz6ZP//5zxk9enSSpKmpKS+88EJWrVpVrLn11lvT1dWVAw44oFizfPnybNq0qVizdOnS7LLLLpu9dS/56+TqdXV13RYAAAAAek9ZQ6m1a9dm9erVWb16dZJkzZo1Wb16dVpaWrJ27dp88YtfzN13353/+q//yrJly/Lxj388O+20U5qbm5Mku+22Ww477LCcdNJJueeee3LXXXdl9uzZOfroozNmzJgkybHHHpvq6urMnDkzDz30UK699tpcdtllmTNnTrlOGwAAAKDilTWUuvfee/Pe9743733ve5Mkc+bMyXvf+96cffbZGTx4cB544IF87GMfy84775yZM2dmv/32yy9/+cvU1NQUj3H11Vdn1113zaGHHpqPfvSj+eAHP5gFCxYU99fX1+fmm2/OmjVrst9+++ULX/hCzj777Jx88sklP18AAAAA/qqsE51Pnjw5hULhNfffdNNNb3iMkSNH5pprrnndmr322iu//OUve9wfAAAAAH1jq5pTCgAAAICBoceh1BNPPJEnn3yyuH7PPffktNNO63bLHAD0lPEFAAAqS49DqWOPPTa33XZbkqS1tTUf+chHcs899+TMM8/M+eef3+sNAlAZjC8AAFBZehxKPfjgg3n/+9+fJFm8eHH22GOPrFixIldffXUWLlzY2/0BUCGMLwAAUFl6HEpt2rSp+PS7W265JR/72MeSJLvuumuefvrp3u0OgIphfAEAgMrS41Bq9913z/z58/PLX/4yS5cuzWGHHZYkeeqpp/K2t72t1xsEoDIYXwAAoLL0OJT6yle+km9961uZPHlyjjnmmOy9995Jkuuvv7542wUA9JTxBQAAKsuQnr5g8uTJefbZZ9PR0ZHtt9++uP3kk0/ONtts06vNAVA5jC8AAFBZenylVJIUCoWsWrUq3/rWt/Liiy8mSaqrq/3SAMBbYnwBAIDK0eMrpR5//PEcdthhaWlpSWdnZz7ykY9kxIgR+cpXvpLOzs7Mnz+/L/oEYIAzvgAAQGXp8ZVSp556avbff/88//zzGTZsWHH7//yf/zPLli3r1eYAqBzGFwAAqCw9vlLql7/8ZVasWJHq6upu29/5znfmj3/8Y681BkBlMb4AAEBl6fGVUl1dXXn55Zdftf3JJ5/MiBEjeqUpACqP8QUAACpLj0OpqVOn5mtf+1pxvaqqKmvXrs0555yTj370o73ZGwAVxPgCAACVpce371188cVpbm7OxIkTs2HDhhx77LH5/e9/nx122CH//u//3hc9AlABjC8AAFBZehxK7bjjjvnP//zPLFq0KA888EDWrl2bmTNn5rjjjus2MS0A9ITxBQAAKkuPQ6kkGTJkSD796U/3di8AVDjjCwAAVI4eh1Lf+973Xnf/jBkz3nQzAFQu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",
      "text/plain": [
       "<Figure size 1200x800 with 5 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "numeric_df = df.select_dtypes(include=['number'])\n",
    "\n",
    "Q1 = numeric_df.quantile(0.25)\n",
    "Q3 = numeric_df.quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    "\n",
    "min_values = Q1 - 1.5 * IQR\n",
    "max_values = Q3 + 1.5 * IQR\n",
    "\n",
    "for column in ['Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Yield']:\n",
    "    df = df[(df[column] > min_values[column]) & (df[column] < max_values[column])]\n",
    "\n",
    "plt.figure(figsize=(12, 8))\n",
    "for i, column in enumerate(['Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Yield'], start=1):\n",
    "    plt.subplot(2, 3, i)\n",
    "    sns.boxplot(df[column])\n",
    "    plt.title(f'Boxplot of {column}')\n",
    "    plt.ylabel('Values')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9c532031-9a0b-40f9-b550-3fd04b88ce0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predicted Yield: [0.70443713]\n",
      "Accuracy (R-squared score): 90.66120108702023 %\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.metrics import r2_score\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "\n",
    "\n",
    "selected_columns = ['Crop', 'Crop_Year', 'Season', 'State', 'Area', 'Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Yield']\n",
    "categorical_cols = ['Crop', 'Season', 'State']\n",
    "numerical_cols = ['Crop_Year', 'Area', 'Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide']\n",
    "\n",
    "preprocessor = ColumnTransformer(\n",
    "    transformers=[\n",
    "        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)\n",
    "    ],\n",
    "    remainder='passthrough'\n",
    ")\n",
    "\n",
    "\n",
    "model = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "\n",
    "\n",
    "pipeline = Pipeline(steps=[('preprocessor', preprocessor),\n",
    "                           ('model', model)])\n",
    "\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(df[selected_columns[:-1]], df['Yield'], test_size=0.2, random_state=42)\n",
    "\n",
    "\n",
    "pipeline.fit(X_train, y_train)\n",
    "\n",
    "\n",
    "user_input = {\n",
    "    'Crop': 'Jute',\n",
    "    'Crop_Year': 1997,\n",
    "    'Season': 'Kharif',\n",
    "    'State': 'Assam',\n",
    "    'Area': 94520.0,\n",
    "    'Production': 904095,\n",
    "    'Annual_Rainfall': 2051.4,\n",
    "    'Fertilizer': 8995468.40,\n",
    "    'Pesticide': 29301.20\n",
    "}\n",
    "\n",
    "user_df = pd.DataFrame([user_input])\n",
    "\n",
    "predicted_yield = pipeline.predict(user_df)\n",
    "print(\"Predicted Yield:\", predicted_yield)\n",
    "\n",
    "y_pred = pipeline.predict(X_test)\n",
    "\n",
    "\n",
    "r2 = r2_score(y_test, y_pred)\n",
    "\n",
    "accuracy_percentage = r2 * 100\n",
    "\n",
    "print(\"Accuracy (R-squared score):\", accuracy_percentage, \"%\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf61ed7a-ff77-41d4-8d5e-14c012192ea1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
