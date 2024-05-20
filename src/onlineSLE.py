import numpy as np
from scipy.fft import fft, fftfreq
from typing import Tuple

def peridogram(sliding_window_size: int, fft_ts : np.ndarray[np.complex128])\
        -> Tuple[np.ndarray, np.ndarray]:
    """
    Peridoogram

    Parameters
    ----------
    sliding_window_size : int
        The sliding window size (N)
    fft_ts : np.ndarray[np.complex128]
        Input FFT signal.
    Returns
    -------
    Tuple :[np.ndarray, np.ndarray]
        Tuple containing the result of Periodogram:
        - xfreq : Array of sample frequencies (np.ndarray).
        - Peridogram :  Peridogram of fft_ts (np.ndarray).

    Note than results are at most half of the maximum signal frequency, due to the Nyquist fundamental theorem.
    """
    periodogram_den = (fft_ts *
                       np.conjugate(fft_ts)) / sliding_window_size
    xfreq = fftfreq(sliding_window_size)[:int(sliding_window_size / 2)]

    return xfreq, periodogram_den[:int(sliding_window_size / 2)].real


def get_period_hints(periodogram_density: np.ndarray[np.complex128]):
    """
    Identify significant periods from a periodogram density.

    Parameters
    ----------
    periodogram_density : np.ndarray[np.complex128]
        Periodogram density, typically obtained from Fourier analysis.

    Returns
    -------
    tuple
        Indices of periods above the threshold and the index of the peak.
    """
    # Extract the real part of the periodogram density
    power = periodogram_density.real

    # Find the index of the peak (maximum power)
    index_peak = np.argmax(power)

    return index_peak


def update_sDFT(fft_X: np.ndarray[np.complex128], old_x: float, new_x: float, twiddle) -> np.ndarray[np.complex128]:
    """
    Update a signal's Discrete Fourier Transform using sliding DFT (sDFT).

    Parameters
    ----------
    fft_X : np.ndarray[np.complex128]
        Previous sDFT.
    old_x : float
        Value to be replaced in the original sDFT.
    new_x : float
        New value to replace the old value.
    twiddle : np.ndarray[np.complex128]
        Twiddle factor (e^{-j2\pi k/N})

    Returns
    -------
    np.ndarray[np.complex128]
        New sDFT.

    References
    ----------
    [1] E. Jacobsen and R. Lyons, "The sliding DFT," in IEEE Signal Processing Magazine,
       vol. 20, no. 2, pp. 74-80, March 2003, doi: 10.1109/MSP.2003.1184347.
    [2] E. Jacobsen and R. Lyons, "An update to the sliding DFT," in IEEE Signal Processing Magazine,
       vol. 21, no. 1, pp. 110-111, Jan. 2004, doi: 10.1109/MSP.2004.1516381.
    """
    new_fft_X = (fft_X - old_x + new_x) * twiddle

    return new_fft_X


def result_aggregation(dataset_name, algo_name, input_results):
    # Define error bounds for evaluating accuracy: 0% (exact match) and 20% (within 20% of the correct answer).
    error_bounds = [0, 20]

    # Initialize a list to store the output results.
    output_results = []

    for error_bound in error_bounds:
        count_result = 0
        for row in input_results:
            # If the error bound is 0, set both lower and upper bounds to the exact answer.
            if error_bound == 0:
                lb = row['answer']  # Lower bound is the exact answer.
                ub = row['answer']  # Upper bound is also the exact answer.
            else:
                # For error bounds other than 0, calculate lower and upper bounds based on the error percentage.
                lb = row['answer'] * ((100 - error_bound) / 100)  # Lower bound adjusted by error percentage.
                ub = row['answer'] * ((100 + error_bound) / 100)  # Upper bound adjusted by error percentage.

            pred_result = row['result']
            if (lb <= pred_result) & (pred_result <= ub):
                count_result = count_result + 1

        # Calculate the accuracy ratio as the number of results within bounds divided by the total number of results.
        accuracy_ratio = count_result / len(input_results)

        # Append the results for the current error bound to the output list.
        output_results.append({
            'dataset_name': dataset_name,
            'algorithms': algo_name,
            'error_bound': error_bound,
            'accuracy_ratio': round(accuracy_ratio, 3)
        })

    # Return the compiled output results.
    return output_results

